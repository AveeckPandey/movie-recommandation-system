import os


TMDB_API_KEY = os.getenv("TMDB_API_KEY", "YOUR_API_KEY")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
DATA_PATH = os.getenv("MOVIE_DATA_PATH", "main_data.csv")
NLP_MODEL_PATH = os.getenv("NLP_MODEL_PATH", "nlp_model.pkl")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH", "tranform.pkl")
