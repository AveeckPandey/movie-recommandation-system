import os


def load_env_file(path=".env"):
    if not os.path.exists(path):
        return

    with open(path, "r") as env_file:
        for line in env_file:
            clean_line = line.strip()
            if not clean_line or clean_line.startswith("#") or "=" not in clean_line:
                continue
            key, value = clean_line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


load_env_file()

TMDB_API_KEY = os.getenv("TMDB_API_KEY", "YOUR_API_KEY")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
DATA_PATH = os.getenv("MOVIE_DATA_PATH", "main_data.csv")
NLP_MODEL_PATH = os.getenv("NLP_MODEL_PATH", "nlp_model.pkl")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH", "tranform.pkl")
