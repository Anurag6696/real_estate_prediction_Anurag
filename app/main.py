from fastapi import FastAPI
from app.schemas.prediction import PredictionInput, PredictionOutput
from app.services.predict import make_prediction

app = FastAPI(title="Real Estate Price Prediction API")

@app.post("/predict", response_model=PredictionOutput)
async def predict_price(input_data: PredictionInput):
    prediction = make_prediction(input_data)
    return PredictionOutput(price=prediction)
