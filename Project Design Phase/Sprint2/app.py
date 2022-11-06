import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
import inputscript
app=Flask(__name__)
model=pickle.load(open('C:\Users\Shruthilaya\phish sample\Phishing_Website.pkl','rb'))
@app.route('/predict')
def predict():
    url=request.form['URL']
    checkprediction=inputscript.main(url)
    prediction=model.predict(checkprediction)
    print(prediction)
    output=prediction[0]
    if output==1:
        pred="This is a legitimate website"
    else:
        pred="This site is unsafe"
    return render_template('final.html',prediction_text='{}'.format(pred),url=url)
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.get_json(force=True)
    prediction=model.y_predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)