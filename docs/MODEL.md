# Model Files

The sentiment analysis flow depends on two pickle files:

- `nlp_model.pkl`
- `tranform.pkl`

`nlp_model.pkl` contains the trained classifier. `tranform.pkl` contains the text transformer used before prediction.

Keep both files in the project root unless you override their paths with environment variables.
