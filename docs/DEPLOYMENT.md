# Deployment

The repository includes a `Procfile` for platforms that run Python web apps with Gunicorn.

Before deployment:

- Configure `TMDB_API_KEY`
- Keep `main_data.csv` in the deployed app
- Keep both pickle model files available
- Disable Flask debug mode

The default debug mode is disabled through `FLASK_DEBUG=false`.
