from fastapi import FastAPI, Form, HTTPException
import pandas as pd
import numpy as np
import logging
import joblib
import json
import sys
import os

# Current directory
current_dir = os.path.dirname(__file__)

# FastAPI app
app = FastAPI()

# Logging
logging.basicConfig(level=logging.ERROR)

# Function
def ValuePredictor(data: pd.DataFrame):
    # Model name
    model_name = 'bin/Logistic_Regression_model.pkl'
    # Directory where the model is stored
    model_dir = os.path.join(current_dir, model_name)
    # Load the model
    loaded_model = joblib.load(open(model_dir, 'rb'))
    # Predict the data
    result = loaded_model.predict(data)
    return result[0]

# Home page
@app.get("/")
def home():
    return {"message": "Welcome to the Loan Prediction API!"}

# Prediction page
@app.post("/prediction")
def predict(name: str = Form(...), 
            application_submission_type: str = Form(...), 
            residential_state: str = Form(...), 
            marital_status: str = Form(...),
            residence_type: str = Form(...),
            monthly_income_tot: str = Form(...),
            sex: float = Form(...),
            flag_residencial_phone: float = Form(...),
            flag_professional_phone: float = Form(...),
            payment_day: float = Form(...),
            nacionality: float = Form(...),
            flags_cards: float = Form(...),
            quant_banking_accounts_tot: float = Form(...),
            personal_assets_value: float = Form(...),
            quant_cards: float = Form(...),
            quant_dependants: float = Form(...),
            months_in_residence: float = Form(...)):
    
    # Load template of JSON file containing columns name
    # Schema name
    schema_name = 'data/columns_set.json'
    # Directory where the schema is stored
    schema_dir = os.path.join(current_dir, schema_name)
    with open(schema_dir, 'r') as f:
        cols = json.loads(f.read())
    schema_cols = cols['data_columns']

    # Parse the Categorical columns
    # APPLICATION_SUBMISSION_TYPE
    try:
        col = ('APPLICATION_SUBMISSION_TYPE_' + str(application_submission_type))
        if col in schema_cols.keys():
            schema_cols[col] = 1
        else:
            pass
    except:
        pass

    # RESIDENCIAL_STATE
    try:
        col = ('RESIDENCIAL_STATE_' + str(residential_state))
        if col in schema_cols.keys():
            schema_cols[col] = 1
        else:
            pass
    except:
        pass

    # MARITAL_STATUS
    try:
        col = ('MARITAL_STATUS_' + str(marital_status))
        if col in schema_cols.keys():
            schema_cols[col] = 1
        else:
            pass
    except:
        pass

    # RESIDENCE_TYPE
    try:
        col = ('RESIDENCE_TYPE_' + str(residence_type))
        if col in schema_cols.keys():
            schema_cols[col] = 1
        else:
            pass
    except:
        pass

    # MONTHLY_INCOMES_TOT
    try:
        col = ('MONTHLY_INCOMES_TOT_' + str(monthly_income_tot))
        if col in schema_cols.keys():
            schema_cols[col] = 1
        else:
            pass
    except:
        pass

    # Parse the Numerical columns
    schema_cols['SEX'] = sex
    schema_cols['FLAG_RESIDENCIAL_PHONE'] = flag_residencial_phone
    schema_cols['COMPANY'] = flag_professional_phone
    schema_cols['PAYMENT_DAY'] = payment_day
    schema_cols['NACIONALITY'] = nacionality
    schema_cols['FLAG_CARDS'] = flags_cards
    schema_cols['QUANT_BANKING_ACCOUNTS_TOT'] = quant_banking_accounts_tot
    schema_cols['PERSONAL_ASSETS_VALUE'] = personal_assets_value
    schema_cols['QUANT_CARS'] = quant_cards
    schema_cols['QUANT_DEPENDANTS'] = quant_dependants
    schema_cols['MONTHS_IN_RESIDENCE'] = months_in_residence

    # Convert the JSON into data frame
    df = pd.DataFrame(data={k: [v] for k, v in schema_cols.items()}, dtype=float)

    # Create a prediction
    result = ValuePredictor(data=df)

    # Determine the output
    if int(result) == 1:
        prediction = f'Dear Mr/Mrs/Ms {name}, your loan is approved!'
    else:
        prediction = f'Sorry Mr/Mrs/Ms {name}, your loan is rejected!'

    # Return the prediction
    return {"prediction": prediction}
