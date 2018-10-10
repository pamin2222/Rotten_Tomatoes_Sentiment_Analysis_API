from main_predictor.classifier import SentimentClassifier
from common.object_pattern import Singleton


class Predictor(Singleton):

    def __init__(self):
        super().__init__()

    def _initialize_model(self):
        self._sentiment_clf = SentimentClassifier()

    def predict_list_text(self, msg_ids=[None], texts=[None]):
        if msg_ids == [None]:
            msg_ids = [None] * len(texts)
        results = self._sentiment_clf.predict(sentence_list=texts)
        # results: [['Negative', 0.7472516298294067], ['Somewhat Positive', 0.4921582341194153], ['Positive', 0.7909849286079407]]

        data = {"success": False}
        data["predictions"] = []
        # loop over the results and add them to the list of
        # returned predictions
        for msg_id, pred_item in zip(msg_ids, results):
            label = pred_item[0]
            prob = pred_item[1]
            r = {"msg_id": msg_id, "label": label, "probability": float(prob)}
            data["predictions"].append(r)

        # indicate that the request was a success
        data["success"] = True
        return data

    def predict_post_request(self, input_json):
        msg_ids = [x.get('msg_id', None) for x in input_json]
        texts = [x.get('text', '') for x in input_json]

        pred_results = self.predict_list_text(msg_ids=msg_ids, texts=texts)
        return pred_results


if __name__ == '__main__':
    in_ = [
        'I love this movie!', 'I hate this movie...']

    # from pprint import pprint
    #
    # predictor = Predictor()
    # predictor._initialize_model()
    # pred_result = predictor.predict_list_text(msg_ids=[1, 2], texts=in_)
    # pprint(pred_result)

    from pprint import pprint

    input_json = [{"msg_id": "1", "text": "I love this movie!"}, {"msg_id": "2", "text": "I hate this movie..."}]
    predictor = Predictor()
    predictor._initialize_model()
    pred_result = predictor.predict_post_request(input_json)
    pprint(pred_result)
