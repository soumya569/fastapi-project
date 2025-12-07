from fastapi import FastAPI
from pydantic import BaseModel
from app.core.dependencies import get_api_key,get_current_user
from app.services.model_service import predict_car_price

router = APIRouter()

class CarFeature(BaseModel):
    company:str
    year:int
    owner:str
    fuel:str
    seller_type:str
    transmission:str
    km_driven:float
    mileage_mpg:float
    engine_cc:float
    torque_nm:float
    seats:float

@router.post("/predict")
def predict_price(car:CarFeatures,user=Depends(get_current_user),_=Depends(get_api_key)):
    prediction = predict_car_price(car.model_dump())
    return {"predicted_price":f'{prediction:,.2f}'}
