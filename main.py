from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


# Set up the app

app = FastAPI(
    title="House Price Predictor",
    description="Predicts house prices",
    version="1.0.0"
)


model = joblib.load("house_model.pkl")






#Pydandtic validation

class theInputs(BaseModel):
    crim: float
    zn: float
    indus: float
    chas: float
    nox: float
    rm: float
    age: float
    dis: float
    rad: float
    tax: float
    ptratio: float
    b: float
    lstat: float





# Endpoints

@app.get("/")
def root():
    return {"message": "Boston house price predictor API", "status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(input: theInputs):
    input_df = pd.DataFrame([input.dict()])

    prediction = model.predict(input_df)[0]


    return {
        "Avg Price": float(prediction),
        "details": input.dict()
    }