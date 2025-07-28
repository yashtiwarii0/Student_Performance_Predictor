from flask import Flask,request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, predict_pipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            request.form.get('gender'),
            request.form.get('race_ethinicity'),
            request.form.get('parental_level_of_education'),
            request.form.get('lunch'),
            request.form.get('test_preparation_course'),
            float(request.form.get('reading_score')),
            float(request.form.get('writing_score'))
        )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)
        predict_pipeline_obj = predict_pipeline()
        results = predict_pipeline_obj.predict(pred_df)
        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
        