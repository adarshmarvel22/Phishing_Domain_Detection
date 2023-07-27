import os
import sys

from flask import Flask, render_template, request, redirect
import numpy as np
import warnings
import pickle 
from src.utils import load_object

warnings.filterwarnings('ignore')
from feature import FeatureExtraction

from src.exception import CustomException
from src.logger import logging 

from src.pipeline.train_pipeline import TraininingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline

# print("model load start")

model_path=os.path.join('artifacts','model.pkl')
file = open(model_path,"rb")
model = pickle.load(file)
file.close()

# print("model load end")

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def index():
    if request.method == "POST":

        url = request.form["input"]
        obj = FeatureExtraction()
        obj.generate_dataframe_from_url(url)

        x = np.array(obj.getFeaturesList()).reshape(1,25) 

        y_pred =model.predict(x)[0]
        
        y_pro_phishing = model.predict_proba(x)[0,0]
        y_pro_non_phishing = model.predict_proba(x)[0,1]
       
        if y_pred == 1:
            result = f"  The site is {round(y_pro_non_phishing,2)*100} % safe ✅"
        else:
            result = f"The site is {round(y_pro_phishing,2)*100} % unsafe ❌"
        return render_template('index.html',result = result)
    return render_template("index.html")

@app.route("/train")
def train_route():
    try:
        train_pipeline = TraininingPipeline()
        train_pipeline.run_pipeline()

        return "Training Completed."

    except Exception as e:
        raise CustomException(e,sys)

@app.route('/report')
def report():
   return render_template('index.html')

@app.route('/data')
def data():
    return redirect('https://www.sciencedirect.com/science/article/pii/S2352340920313202')

if __name__ == '__main__':
    app.run(debug=True)
