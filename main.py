# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to your MLOps pipeline!"}

@app.post("/predict")
async def predict(data: dict):
    # Mock prediction logic
    prediction = sum(data.values())
    return {"prediction": prediction}
