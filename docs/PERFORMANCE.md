# Performance Notes

The similarity matrix can be expensive to build, so the app now keeps it in memory after the first calculation.

Potential future improvements:

- Precompute similarity scores
- Cache TMDB responses
- Cache IMDb review responses
- Limit blocking frontend requests
- Add pagination for large result sets
