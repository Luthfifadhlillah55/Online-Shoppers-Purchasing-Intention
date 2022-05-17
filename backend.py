from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("model_rf_classifier.pkl", "rb") as f:
    model = pickle.load(f)

columns = ['Administrative', 'Administrative_Duration', 'ProductRelated',
       'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues',
       'TrafficType', 'VisitorType_Other', 'VisitorType_Returning_Visitor',
       'Weekend_True', 'Month_sin', 'Month_cos', 'SpecialDay_1',
       'OperatingSystems_2', 'OperatingSystems_3', 'OperatingSystems_other',
       'Browser_2', 'Browser_other', 'Region_2', 'Region_3', 'Region_4',
       'Region_5', 'Region_6', 'Region_7', 'Region_8', 'Region_9']
classes = ['No to Buy', 'To Buy']

@app.route("/")
def home():
    return "<h1>It Works!</h1>"

@app.route("/predict", methods=['GET','POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        try:
            data= [content['Administrative'],
                   content['Administrative_Duration'],
                   content['ProductRelated'],
                   content['ProductRelated_Duration'],
                   content['BounceRates'],
                   content['ExitRates'],
                   content['PageValues'],
                   content['TrafficType'],
                   content['VisitorType_Other'],
                   content['VisitorType_Returning_Visitor'],
                   content['Weekend_True'],
                   content['Month_sin'],
                   content['Month_cos'],
                   content['SpecialDay_1'],
                   content['OperatingSystems_2'],
                   content['OperatingSystems_3'],
                   content['OperatingSystems_other'],
                   content['Browser_2'],
                   content['Browser_other'],
                   content['Region_2'],
                   content['Region_3'],
                   content['Region_4'],
                   content['Region_5'],
                   content['Region_6'],
                   content['Region_7'],
                   content['Region_8'],
                   content['Region_9']]
                     
            data = pd.DataFrame([data], columns=columns)
            res = model.predict(data)
            response = {"code": 200, "status":"OK", 
                        "result":{"prediction":str(res[0]),
                                   "description":classes[res[0]]}}
            return jsonify(response)
        except Exception as e:
            response = {"code":500, "status":"ERROR", 
                        "result":{"error_msg":str(e)}}
            return jsonify(response)
    return "<p>Silahkan gunakan method POST untuk mengakses hasil prediksi dari model</p>"