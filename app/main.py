from fastapi import FastAPI
from pydantic import BaseModel
import joblib
#from schemas import HeartDiseaseInput

# Load the trained model
model = joblib.load('model/heart_model.joblib')

app = FastAPI()

class HeartDiseaseInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

    
@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/info")
def model_info():
    return {
        "model_type": "Random Forest",
        "features": ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
    }

@app.post("/predict")
def predict(data: HeartDiseaseInput):
    input_data = [[
        data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs, data.restecg,
        data.thalach, data.exang, data.oldpeak, data.slope, data.ca, data.thal
    ]]
    
    prediction = model.predict(input_data)
    
    return {"heart_disease": bool(prediction[0])}
