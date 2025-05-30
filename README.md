# MLOps Model Deployment: FastAPI + Docker

This project demonstrates how to deploy a trained ML model as a REST API using FastAPI and Docker.

## How to Run Locally

1. Build the Docker image:
   ```
   docker build -t mlops-api .
   ```
2. Run the container:
   ```
   docker run -p 8000:8000 mlops-api
   ```
3. Test the API (e.g., with curl or Postman):
   ```
   curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"gender":0,"senior":0,"partner":1,"dependents":0,"tenure":12,"monthly":70.0,"total":1000.0}'
   ```

## Free Deployment

- Deploy on [Render](https://render.com), [Railway](https://railway.app), or [Hugging Face Spaces](https://huggingface.co/spaces) (with minor tweaks).

---

## How to Use

1. **Export your trained model** as `model.pkl` (use `joblib.dump(model, "model.pkl")` in your notebook).
2. **Copy all files** into a new folder.
3. **Build and run with Docker** (see README).
4. **Deploy for free** on Render, Railway, or Hugging Face Spaces (all have free tiers).
