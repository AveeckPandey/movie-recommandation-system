# Recommendation Engine

The app uses a content-based recommendation approach.

Steps:

1. Load movie metadata from `main_data.csv`.
2. Vectorize the `comb` column with `CountVectorizer`.
3. Calculate cosine similarity for every movie pair.
4. Return the top matches for the selected movie.

This works best when the selected title exists in the local dataset.
