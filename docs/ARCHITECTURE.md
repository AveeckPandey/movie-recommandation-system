# Architecture

The application has a Flask backend and a browser-based frontend.

## Request Flow

1. The home page loads movie title suggestions from `main_data.csv`.
2. The user searches for a movie in the browser.
3. `static/recommend.js` fetches movie metadata from TMDB.
4. The frontend posts the movie title to `/similarity`.
5. Flask calculates similar movies with cosine similarity.
6. The frontend sends selected movie details to `/recommend`.
7. Flask scrapes IMDb reviews and predicts review sentiment.
8. `templates/recommend.html` renders details, cast, reviews, and recommendations.
