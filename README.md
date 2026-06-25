# Movie Recommendation System with Sentiment Analysis

A Flask-based movie recommendation web application that suggests similar movies and analyzes IMDb user reviews using a trained sentiment analysis model.

The app combines a content-based recommendation engine with live movie metadata from TMDB. Users can search for a movie, view detailed information, explore cast details, see recommended titles, and read sentiment-tagged IMDb reviews.

## Features

- Content-based movie recommendations using cosine similarity
- Movie search with autocomplete suggestions
- TMDB integration for posters, ratings, runtime, genres, cast, and overview
- IMDb review scraping with BeautifulSoup
- Review sentiment classification as Good or Bad
- Flask backend with AJAX-powered frontend flow
- Responsive HTML, CSS, and JavaScript interface

## Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- BeautifulSoup
- HTML, CSS, JavaScript
- AJAX and jQuery
- TMDB API

## Project Structure

```text
.
├── datasets/              # Source and processed dataset files
├── static/                # CSS, JavaScript, images, and loaders
│   ├── autocomplete.js
│   ├── recommend.js
│   └── style.css
├── templates/             # Flask HTML templates
│   ├── home.html
│   └── recommend.html
├── main.py                # Flask app and recommendation routes
├── main_data.csv          # Movie data used for recommendations
├── nlp_model.pkl          # Trained sentiment analysis model
├── tranform.pkl           # Text vectorizer for sentiment analysis
├── requirements.txt       # Python dependencies
└── Procfile               # Deployment process file
```

## How It Works

1. The user searches for a movie from the home page.
2. The frontend calls the TMDB API to fetch movie details.
3. Flask receives the selected movie title and finds similar movies from `main_data.csv`.
4. The recommendation engine builds a count vector matrix from movie metadata and applies cosine similarity.
5. The app scrapes IMDb reviews for the selected movie.
6. The trained NLP model predicts whether each review is positive or negative.
7. The result page displays movie details, cast information, recommendations, and review sentiments.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AveeckPandey/movie-recommandation-system.git
cd movie-recommandation-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your TMDB API Key

Create a TMDB account at [themoviedb.org](https://www.themoviedb.org/) and generate an API key from your account settings.

Copy `.env.example` to `.env`, then replace the placeholder value with your TMDB API key.

```text
TMDB_API_KEY=your_tmdb_api_key_here
```

### 5. Run the Application

```bash
python main.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000/
```

## Recommendation Logic

The recommender is content-based. It compares movies using text features stored in the `comb` column of `main_data.csv`.

The process is:

- Convert combined movie metadata into vectors using `CountVectorizer`
- Calculate similarity between movie vectors using cosine similarity
- Sort movies by similarity score
- Return the top 10 closest matches

Cosine similarity measures how close two vectors are by comparing the angle between them. A higher score means the movies are more similar based on their metadata.

## Sentiment Analysis

The app uses:

- `nlp_model.pkl` for the trained sentiment classifier
- `tranform.pkl` for transforming review text into model-ready features

IMDb reviews are scraped for the selected movie, transformed with the vectorizer, and classified as either Good or Bad.

## Dataset Sources

The recommendation dataset is built from movie metadata collected from public movie datasets and movie lists, including:

- IMDb 5000 Movie Dataset
- The Movies Dataset
- American film lists from 2018, 2019, and 2020

## Notes

- A TMDB API key is required for movie details, posters, cast, and recommendations.
- IMDb page structure may change over time, which can affect review scraping.
- The app uses local `.pkl` model files, so keep them in the project root when running the app.

## Additional Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Local Setup](docs/SETUP.md)
- [TMDB API Key](docs/API_KEY.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Deployment](docs/DEPLOYMENT.md)

## License

This project is intended for learning and educational use.
