import pickle
from flask import Flask
from flask import request
from flask import jsonify


input = 'diabetes_dv_and_xgboost.bin'
with open(input, 'rb') as file:
    dv, model = pickle.load(file)

app = Flask('diabetes')

@app.route('/diabetes', methods=['POST'])
def predict_score():
    patient = request.get_json()
    vectorized = dv.transform(patient)
    y_pred = model.predict_proba(vectorized)[0,1]
    result = {
        'predicted_score': ['no risk' if float(y_pred)<0.5 else 'risk']
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
