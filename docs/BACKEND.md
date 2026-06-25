# Backend Notes

The Flask app is defined in `main.py`.

Routes:

- `/` and `/home` render the search page
- `/similarity` returns recommended movie titles
- `/recommend` renders the movie details page

The backend loads the recommendation dataset and sentiment model files from local project paths.
