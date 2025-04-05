import numpy as np
from app.schemas.prediction import PredictionInput

def preprocess_input(input_data: PredictionInput) -> np.ndarray:
    # Example preprocessing; adjust based on your model's requirements
    location_encoded = hash(input_data.location) % 1000
    return np.array([[input_data.area, input_data.bedrooms, input_data.bathrooms, location_encoded]])
