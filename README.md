# MLOps Model Deployment: FastAPI + Docker + Web UI

This project demonstrates how to deploy a trained ML model as a REST API using FastAPI and Docker, with a simple web UI for user-friendly predictions.

## Features

- **Machine Learning Model**: RandomForestClassifier trained to predict customer churn.
- **API**: FastAPI backend serving predictions at `/predict`.
- **Web UI**: User-friendly form at `/` (http://localhost:8000/) for interactive predictions.
- **Dockerized**: Easily build and run anywhere with Docker.

## How to Run Locally

1. Build the Docker image:
   ```
   docker build -t mlops-api .
   ```
2. Run the container:
   ```
   docker run -p 8000:8000 mlops-api
   ```
3. Open your browser and go to:
   [http://localhost:8000/](http://localhost:8000/)
4. Fill out the form and click Predict to get a churn prediction.

Or, test the API directly:
   ```
   curl -Method POST -Uri "http://localhost:8000/predict" -ContentType "application/json" -Body '{"gender":0,"senior":0,"partner":1,"dependents":0,"tenure":12,"monthly":70.0,"total":1000.0}'
   ```

## Free Deployment

- Deploy on [Render](https://render.com), [Railway](https://railway.app), or [Hugging Face Spaces](https://huggingface.co/spaces) (with minor tweaks).

---

## How to Use

1. **Export your trained model** as `model.pkl` (use `joblib.dump(model, "model.pkl")` in your notebook).
2. **Copy all files** into a new folder.
3. **Build and run with Docker** (see above).
4. **Access the web UI** at [http://localhost:8000/](http://localhost:8000/).
5. **Deploy for free** on Render, Railway, or Hugging Face Spaces (all have free tiers).

---

## Example Screenshot

![Web UI Screenshot](static/example-screenshot.png)

---

## Project Structure

```
main.py            # FastAPI app
model.pkl          # Trained ML model
requirements.txt   # Python dependencies
Dockerfile         # Docker build file
static/index.html  # Web UI
README.md          # Project documentation
```

---

## License

MIT
