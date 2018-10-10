## Sentiment Analysis API

### Datasets
Sentiment model is trained using Rotten Tomatoes dataset from 
https://www.kaggle.com/c/movie-review-sentiment-analysis-kernels-only/data

### How to Create and run rotten_tomatos_sentiment_predictor docker container
```
# Remove old image 
docker rmi $(docker images | grep 'rotten_tomatoes_sentiment')
```

```
docker build . -t rotten_tomatoes_sentiment:0_0_1
docker run -d -p 2209:11005 rotten_tomatoes_sentiment:0_0_1
```

Then try access an API via
```http://[your_ip_address]:2209```