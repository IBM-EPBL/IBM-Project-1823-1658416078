import numpy as np
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
import pickle
import inputScript
app=Flask(__name__)
CORS(app)
model=pickle.load(open('Phishing_Website.pickle.dat','rb'))
@app.route('/ypredict',methods=['POST'])
def y_predict():
    data = request.get_json(force=True)
    URL = data.get('URL')
    checkprediction= inputScript.main(URL)
    print("checkprediction",checkprediction)
    prediction=model.predict(checkprediction)
    print("predict answer in binary" , prediction)
    output=prediction[0]
    print("output" , output)
    if output==1:
        pred = "This is a legitimate website"
        status = "green"
    else:
        pred = "This site is unsafe"
        status = "red"
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