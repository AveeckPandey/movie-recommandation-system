# Testing Notes

There is no formal test suite yet.

Manual checks:

- Home page loads without errors
- Autocomplete displays movie suggestions
- Search shows movie details
- Similarity route returns recommendations
- Recommendation page renders even when IMDb reviews are unavailable

Future tests should cover `convert_to_list`, `rcmd`, and route responses.
