# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:11:32 2020

@author: Pratik
"""


from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

with open('HDClassifierRF.pkl','rb')as pickle_file:
    model=pickle.load(pickle_file)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    
    
    
    if request.method == 'POST':
        
        custid = int(request.form['custid'])
        
        CreditScore = int(request.form['Credit_score'])
        Age = int(request.form['Age'])
        Tenure = int(request.form['tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = int(request.form['Noproduct'])
        EstimatedSalary= float(request.form['EstimatedSalary'])
        
        HasCrCard = request.form['credit_card']
        if(HasCrCard=='Yes'):
            HasCrCard=1
        else:
            HasCrCard=0
            
        IsActiveMember = request.form['IsActiveMember']
        if(IsActiveMember=='Yes'):
            IsActiveMember=1
        else:
            IsActiveMember=0
        
        Gender = request.form['Gender']
        if(Gender=='Male'):
            Gender_Male=1
        else:
            Gender_Male=0
            
        Geography = request.form['Geography']
        if(Geography=='Germany'):
                Geography_Germany=1
                Geography_Spain=0
        elif(Geography=='Spain'):
                Geography_Germany=0
                Geography_Spain=1
        else:
            Geography_Germany=0
            Geography_Spain=0
        
        
        prediction=model.predict([[CreditScore, Age, Tenure, Balance,NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary,Geography_Germany, Geography_Spain, Gender_Male]])
        output=prediction[0]
        if output ==0:
           return render_template('index.html',prediction_text = "Customer is not going to Churn")
        else:
           return render_template('index.html',prediction_text = "Customer  is going to churn ")
    #else:
      # return render_template('index.html')

if __name__=="__main__":
    app.run()