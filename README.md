# End-to-End ML Project

An end-to-end machine learning pipeline with modular components for data ingestion,
data transformation, and model training, with experiment tracking via MLflow and DagsHub.

## Project Structure

- `src/mlproject/components/` — data ingestion, transformation, and model training modules
- `src/mlproject/logger.py` — custom logging setup
- `src/mlproject/exception.py` — custom exception handling
- `app.py` — main training pipeline entry point

## Tech Stack

- Python, scikit-learn, pandas, numpy
- MLflow + DagsHub for experiment tracking
- Flask
- Docker

## Setup

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your DagsHub credentials (see `.env.example`)
4. Run: `python app.py`

## Results

(add your model's metrics here once you have them — RMSE, R², etc.)
