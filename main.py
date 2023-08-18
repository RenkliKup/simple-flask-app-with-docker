from flask import Flask,jsonify,request
import pandas as pd
import joblib

loaded_model=""
Filepath='./model/random_forest_model.pkl'
with open(Filepath, 'rb') as model_file:
        loaded_model = joblib.load(model_file)


app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    
    json = request.get_json()
    print(json)
    
    df = pd.DataFrame(json, index=[0])
    x = pd.DataFrame(df)
    predict = loaded_model.predict(x).tolist()
     
    res= {"Outcome" : predict}
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

