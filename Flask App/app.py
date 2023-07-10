from flask import Flask, render_template, url_for,request
import pickle as p
import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



modelfile = 'models/final_prediction.pickle'  
model = p.load(open(modelfile, 'rb'))
scaler= pickle.load(open('models/scaler.pickle','rb'))
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/predict',methods =['GET','POST'])
def predict():
    Nitrogen = float(request.form["Nitrogen"])
    phosphorus =float(request.form['phosphorus'])
    Potassium = float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    humidity = float(request.form['humidity'])
    ph  = float(request.form['ph'])
    rainfall= float(request.form['rainfall'])
 

    total = [[Nitrogen,phosphorus,Potassium,Temperature,humidity,ph,rainfall]]
    prediction = model.predict(scaler.transform(total))
    prediction = int(prediction[0])

    if prediction==0:
        return render_template('index.html',predict="apple")
    
    if prediction==1:
        return render_template('index.html',predict="banana")
    if prediction==2:
        return render_template('index.html',predict="blackgram")
    
    if prediction==3:
        return render_template('index.html',predict="chickpea")
    if prediction==4:
        return render_template('index.html',predict="coconut")
    
    if prediction==5:
        return render_template('index.html',predict="coffee")
    if prediction==6:
        return render_template('index.html',predict="cotton")
    
    if prediction==7:
        return render_template('index.html',predict="grapes")

    if prediction==8:
        return render_template('index.html',predict="jute")
    
    if prediction==9:
        return render_template('index.html',predict="kidneybeans")
    if prediction==10:
        return render_template('index.html',predict="lentil")
    
    if prediction==11:
        return render_template('index.html',predict="maize")
          
    if prediction==12:
        return render_template('index.html',predict="mango")
    
    if prediction==13:
        return render_template('index.html',predict="mothbeans")
    if prediction==14:
        return render_template('index.html',predict="mungbean")
    
    if prediction==15:
        return render_template('index.html',predict="muskmelon")
    if prediction==16:
        return render_template('index.html',predict="orange")
    
    if prediction==17:
        return render_template('index.html',predict="papaya")
    if prediction==18:
        return render_template('index.html',predict="pigeonpeas")
    
    if prediction==19:
        return render_template('index.html',predict="pomegranate")
    
    if prediction==20:
        return render_template('index.html',predict="rice")
       
    else:
        return render_template('index.html',predict="watermelon")  

    




if __name__ == '__main__':
    app.run(debug=True)
