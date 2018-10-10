from classifier_nn.classifier import SentimentNNClassifier
import numpy as np
from utils import label_util
from common.object_pattern import Singleton


class SentimentClassifier(Singleton):
    def __init__(self):
        super().__init__()
        self.classifier = SentimentNNClassifier()

    def predict(self, sentence_list):
        pred_probs = self.classifier.predict_proba(sentence_list)
        result = list(map(self._format_answer, pred_probs))
        return result

    def _format_answer(self, pred_prob):
        pred_class_num = int(np.argmax(pred_prob))
        pred_class_prob = float(pred_prob[pred_class_num])
        pred_class_name = label_util.clf_pred_num_to_cls_name(pred_class_num)
        single_result = [pred_class_name, pred_class_prob]
        return single_result


if __name__ == "__main__":
    sen_clf = SentimentClassifier()
    pred_results = sen_clf.predict(["Bad Movie", "Good Movie", "Superb Movie"])
    print("pred_results:", pred_results)
