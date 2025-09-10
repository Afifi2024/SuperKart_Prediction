import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask("SuperKart Predictor")

# Load model and encoders
model = joblib.load("XG_best_model.joblib")
label_encoders = joblib.load("label_encoders.joblib")

@app.route('/', methods=['GET'])
def home():
    return "<h1>SuperKart Predictor</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.get_json()
    df = pd.DataFrame([data])

    # Apply same encoding as training
    for column, encoder in label_encoders.items():
        df[column] = encoder.transform(df[column])

    # Add store_history feature
    df['store_history'] = 2025 - df['Store_Establishment_Year']

    # Drop columns not needed for prediction
    df.drop(columns=['Product_Id', 'Store_Id', 'Store_Establishment_Year'], inplace=True)

    # Make prediction
    prediction = model.predict(df)[0]

    return jsonify({"Prediction": str(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
