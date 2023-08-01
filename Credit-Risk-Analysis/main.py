# main.py
from fastapi import FastAPI, Form, HTTPException
import pandas as pd
import logging
import joblib
import redis
import os
import json

app = FastAPI()
logging.basicConfig(level=logging.ERROR)

# Function to predict loan approval
def predict_loan_approval(input_data):
    # Replace this with your actual machine learning model prediction code
    # For demonstration purposes, we'll return a random prediction (0 or 1)
    import random
    return random.randint(0, 1)

# Initialize Redis client
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

# Home page
@app.get("/")
def home():
    return {"message": "Welcome to the Loan Prediction API!"}

# Prediction page
@app.post("/prediction")
def predict(name: str = Form(...),
            # Add other form fields here based on your form
           ):
    # Combine form fields into a dictionary to represent the input data
    input_data = {
        "name": name,
        # Add other form fields as key-value pairs here
    }

    # Convert input data to a DataFrame (replace this with your data preprocessing)
    df = pd.DataFrame([input_data])

    # Check if the prediction is cached in Redis
    cache_key = json.dumps(input_data, sort_keys=True)
    cached_prediction = redis_client.get(cache_key)
    if cached_prediction is not None:
        prediction = int(cached_prediction)
    else:
        # Make the prediction
        prediction = predict_loan_approval(df)
        # Cache the prediction in Redis for future use
        redis_client.set(cache_key, prediction)

    # Determine the output message based on the prediction
    if prediction == 1:
        output_msg = f"Dear Mr/Mrs/Ms {name}, your loan is approved!"
    else:
        output_msg = f"Sorry Mr/Mrs/Ms {name}, your loan is rejected!"

    # Return the prediction result as a JSON response
    return {"prediction": output_msg}
