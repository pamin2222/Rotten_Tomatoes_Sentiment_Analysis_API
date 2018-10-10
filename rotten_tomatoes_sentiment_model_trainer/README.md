## Rotten Tomatoes Sentiment Model Trainer

This repository contains notebook file for model training.

#### Training Environment
The same training environment can be created using provided DockerFile

#### Pretrain Weight
"glove.6B.100d.txt" can be dowloaded from https://nlp.stanford.edu/projects/glove/  
or
https://www.kaggle.com/terenceliu4444/glove6b100dtxt

##### Example docker cmd for running training container
```
nvidia-docker build -t rotten_tomatoes_sentiment_trainer .
nvidia-docker run -it --rm -d -p 8832:6006 -p 8833:6007 -v $(pwd):/workdir rotten_tomatoes_sentiment_trainer bash
nvidia-docker ps
nvidia-docker exec -it [container_id] bash
jupyter notebook --port=6006 --allow-root "$@" --ip 0.0.0.0 --no-browser &
```

#### API Deployment 
After model training is done.
There are 3 output files to update to "rotten_tomatoes_sentiment_classifier_api"
- model.hdf5  --> "rotten_tomatoes_sentiment_classifier_api/classifier_nn/models/model.hdf5"
- sentiment_lb.pickle  --> "rotten_tomatoes_sentiment_classifier_api/classifier_nn/models/sentiment_lb.pickle"
- tokenizer.pickle  --> "rotten_tomatoes_sentiment_classifier_api/preprocess/assets/tokenizer.pickle"