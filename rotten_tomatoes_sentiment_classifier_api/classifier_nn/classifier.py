import os
import pickle
from tensorflow.python.keras.models import load_model
from classifier_nn import package_constant
from preprocess import preprocessor
from common.object_pattern import Singleton


class SentimentNNClassifier(Singleton):
    def __init__(self):
        super().__init__()
        self._model, self._lb = self._load_models()

    def _load_models(self):
        latest_model_path = os.path.join(package_constant.CLASSIFIER_NN_ROOT_DIR, "models", "model.hdf5")
        lb_path = os.path.join(package_constant.CLASSIFIER_NN_ROOT_DIR, "models", "sentiment_lb.pickle")
        model = load_model(latest_model_path)
        lb = pickle.load(open(lb_path, 'rb'))
        model._make_predict_function()
        return model, lb

    def predict_proba(self, texts):
        text_seqs = preprocessor.texts_to_pad_seq(texts)
        pred_probs = self._model.predict(text_seqs)
        return pred_probs


if __name__ == "__main__":
    sen_clf = SentimentNNClassifier()
    pred_probs = sen_clf.predict_proba(["Bad Movie", "Good Movie"])
    print("pred_probs:", pred_probs)
