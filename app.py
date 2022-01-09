# import libraries
import numpy as np
import pandas as pd 
from flask import Flask, render_template,render_template_string,request
import pickle # initialize the flask App

app = Flask(__name__, template_folder='templates')

model = pickle.load(open('model.pkl', 'rb')) # load model 

@app.route('/',methods=['POST', 'GET'])
def main():

    if request.method == 'GET':
            return(render_template('main.html'))

    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        chestpaintype = request.form['chestpaintype']
        restingbloodpressure = request.form['restingbloodpressure']
        serumcholesterol = request.form['serumcholesterol']
        fastingbloodsugar = request.form['fastingbloodsugar']
        electrocardiographic = request.form['electrocardiographic']
        maxheartrate = request.form['maxheartrate']
        exerciseinducedangina = request.form['exerciseinducedangina']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        majorvessels = request.form['majorvessels']
        thal = request.form['thal']

        input_variables = pd.DataFrame([[age, sex, chestpaintype, restingbloodpressure,serumcholesterol,fastingbloodsugar,
                                    electrocardiographic,maxheartrate,exerciseinducedangina,oldpeak,slope,majorvessels,thal]],
                                    columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'],
                                    dtype=float)

        prediction = model.predict(input_variables)[0]
        if (prediction == 1): 
            prediction_result = 'This patient is likely to be suffering from heart disease.'
        else: 
            prediction_result = 'This patient is likely to be healthy.'
        
        return render_template('main.html',prediction=prediction_result,show_predictions_modal=True)

if __name__ == "__main__":
    app.run(debug=True)

  
