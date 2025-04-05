import pickle
import numpy as np
from app.utils.preprocess import preprocess_input
from app.schemas.prediction import PredictionInput

# Load the trained model
with open("app/models/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def make_prediction(input_data: PredictionInput) -> float:
    processed_data = preprocess_input(input_data)
    prediction = model.predict(processed_data)
    return np.round(prediction[0], 2)
