from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Serve static files (web UI)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

# Load model
model = joblib.load("model.pkl")

class ChurnInput(BaseModel):
    gender: int
    senior: int
    partner: int
    dependents: int
    tenure: int
    monthly: float
    total: float

@app.post("/predict")
def predict_churn(data: ChurnInput):
    features = np.array([[data.gender, data.senior, data.partner, data.dependents, data.tenure, data.monthly, data.total]])
    pred = model.predict(features)[0]
    return {"churn": int(pred)}
