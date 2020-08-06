from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("zz.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("deploy.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":


        
        MONTH = float(request.form["MONTH"])
        DAY = float(request.form["DAY"])
        DAY_OF_WEEK = float(request.form["DAY_OF_WEEK"])
        AIRLINE = float(request.form["AIRLINE"])
        SCHEDULED_DEPARTURE = float(request.form["SCHEDULED_DEPARTURE"])
        DEPARTURE_TIME = float(request.form["DEPARTURE_TIME"])
        TAXI_OUT = float(request.form["TAXI_OUT"])
        DISTANCE = float(request.form["DISTANCE"])
        TAXI_IN = float(request.form["TAXI_IN"])
        SCHEDULED_ARRIVAL = float(request.form["SCHEDULED_ARRIVAL"])
        ARRIVAL_DELAY = float(request.form["ARRIVAL_DELAY"])
        
        
        prediction=model.predict([[
            MONTH,
            DAY,
            DAY_OF_WEEK,
            AIRLINE,
            SCHEDULED_DEPARTURE,
            DEPARTURE_TIME,
            TAXI_OUT,
            DISTANCE,
            TAXI_IN,
            SCHEDULED_ARRIVAL,
            ARRIVAL_DELAY
        ]])
        
        
        output=round(prediction[0],2)

        return render_template('deploy.html',prediction_text="Airline Delay Should Be in min. {}".format(output))


    return render_template("deploy.html")



if __name__ == "__main__":
    app.run(debug=True)
