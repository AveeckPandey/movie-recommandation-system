# Local Setup

## Requirements

- Python 3.8 or newer
- A TMDB API key
- Internet access for TMDB metadata and IMDb reviews

## Steps

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python main.py
```

Update `.env` with your TMDB API key before searching for movies.

Open `http://127.0.0.1:5000/` in your browser.
