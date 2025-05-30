# Customer Churn Prediction API (MLOps Project)

## Overview

This project is an end-to-end machine learning solution for predicting customer churn in a telecom company. It demonstrates how to train a model, serve it as a REST API using FastAPI, containerize the solution with Docker, and provide a user-friendly web interface for predictions.

## Problem Statement

**Customer churn** is when a customer stops using a company’s service. Predicting churn helps businesses take action to retain valuable customers, reducing revenue loss and improving customer satisfaction.

## Dataset

- **Source:** [IBM Telco Customer Churn Dataset](https://www.ibm.com/communities/analytics/watson-analytics-blog/guide-to-sample-datasets/)
- **Description:** Contains demographic, account, and usage data for telecom customers, along with a churn label indicating if the customer left.
- **Features Used:**
  - gender, SeniorCitizen, Partner, Dependents, tenure, MonthlyCharges, TotalCharges

## Solution Approach

- **Data Preprocessing:** Categorical features are encoded, and missing values are handled.
- **Model:** RandomForestClassifier (scikit-learn) trained to predict the probability of churn.
- **API:** FastAPI serves predictions at `/predict`.
- **Web UI:** A simple form at `/` lets users enter customer data and get instant predictions.
- **Containerization:** Docker ensures the app runs the same everywhere.

## How to Run Locally

1. **Build the Docker image:**
   ```powershell
   docker build -t mlops-api .
   ```
2. **Run the container:**
   ```powershell
   docker run -p 8000:8000 mlops-api
   ```
3. **Open your browser:**
   [http://localhost:8000/](http://localhost:8000/)
4. **Fill out the form and click Predict** to get a churn prediction.

Or, test the API directly:

```powershell
curl -Method POST -Uri "http://localhost:8000/predict" -ContentType "application/json" -Body '{"gender":0,"senior":0,"partner":1,"dependents":0,"tenure":12,"monthly":70.0,"total":1000.0}'
```

## Project Structure

```
main.py            # FastAPI app
model.pkl          # Trained ML model
requirements.txt   # Python dependencies
Dockerfile         # Docker build file
static/index.html  # Web UI
README.md          # Project documentation
```

## License

MIT
