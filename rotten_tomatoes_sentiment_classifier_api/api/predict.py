from .model_fields import model_message
from main_predictor.predictor import Predictor
from flask import request
from flask_restplus import Namespace, Resource
import tensorflow as tf

api = Namespace('predict', description='Prediction Details')
message = api.model('Message', model_message)

predictor = Predictor()
predictor._initialize_model()
graph = tf.get_default_graph()


@api.route('/')
class Predict(Resource):
    @api.expect([message])
    @api.response(200, 'Success')
    def post(self):
        with graph.as_default():
            list_input = request.get_json()
            return predictor.predict_post_request(list_input)
