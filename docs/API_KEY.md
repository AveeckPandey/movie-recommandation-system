# TMDB API Key

The app uses TMDB for movie posters, metadata, cast details, and IDs.

## Recommended Setup

Create a `.env` file locally and add:

```text
TMDB_API_KEY=your_tmdb_api_key_here
```

The sample values live in `.env.example`.

## Frontend Note

The browser must call TMDB directly, so the key is exposed to the frontend at runtime. Use a TMDB key intended for this app.
