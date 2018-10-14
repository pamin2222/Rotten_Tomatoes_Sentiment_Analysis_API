## English Sentiment Analysis API

### Datasets
Sentiment model is trained using Rotten Tomatoes dataset from 
https://www.kaggle.com/c/movie-review-sentiment-analysis-kernels-only/data

#### Model Training
rotten_tomatoes_sentiment_model_trainer


#### Sentiment Analysis API
rotten_tomatoes_sentiment_classifier_api

The API project can be start directly. The model is already there.
If the new model is required, you can retrain it using trainer project. 
It is better to run it with GPU. Training using CPU (use docker and tensorflow CPU version) may take a long time.
