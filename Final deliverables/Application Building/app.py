import numpy as np
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
import pickle
import inputScript
app=Flask(__name__)
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "0uJ9sY18fcEsrF3XRXzMv0pa4S5iSWBOrlETuCHiPKVl"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
CORS(app)
model=pickle.load(open('Phishing_Website.pickle.dat','rb'))
@app.route('/ypredict',methods=['POST'])
def y_predict():
    data = request.get_json(force=True)
    URL = data.get('URL')
    checkprediction= inputScript.main(URL)
    payload_scoring = {"input_data": [{"field": [["UsingIP","LongURL","ShortURL","Symbol@","Redirecting//","PrefixSuffix-","SubDomains","HTTPS","DomainRegLen","Favicon","NonStdPort","HTTPSDomainURL","RequestURL","AnchorURL","LinksInScriptTags","ServerFormHandler","InfoEmail","AbnormalURL","WebsiteForwarding","StatusBarCust","DisableRightClick","UsingPopupWindow","IframeRedirection","AgeofDomain","DNSRecording","WebsiteTraffic","PageRank","GoogleIndex","LinksPointingToPage","StatsReport"
]], "values": checkprediction}]}

    
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3ea4cad9-0a51-41b6-bebb-35aa04a53713/predictions?version=2022-11-18', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
    
    prediction=(response_scoring.json())
   
    predic=prediction['predictions'][0]['values'][0][0]

    
    if(predic==-1):
        pred = "You are safe!! This is a Legimate Website :)"
        status="green"
    elif(predic==1):
        pred = "You are in a phishing site. Dont Trust :("
        status="red"
    else:
        pred = "You are in a suspicious site. Be Cautious ;("
        status="green"
    
    return {
        "url" : URL ,
        "pred" : pred,
        "status" : status,
    }

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.get_json(force=True)
    prediction=model.y_predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)