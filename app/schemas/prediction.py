from pydantic import BaseModel

class PredictionInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    location: str

class PredictionOutput(BaseModel):
    price: float
