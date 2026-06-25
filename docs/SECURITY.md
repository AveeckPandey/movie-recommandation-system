# Security Notes

Do not commit real API keys to the repository.

The app fetches external pages from TMDB and IMDb, so treat remote data as untrusted. Flask templates escape variables by default, which helps reduce accidental injection risks.

For production deployments, keep debug mode disabled.
