from flask import Blueprint
from flask_restplus import Api, Resource
from api.predict import api as predict

blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title='Sentiment Classification API from rotten tomatoes dataset',
          version='0.0.1',
          description='Sentiment Classification API from rotten tomatoes dataset',
          default='about',
          default_label='About API'
          )


@api.route('/about')
class About(Resource):
    def get(self):
        return {'title': 'Sentiment Classification API from rotten tomatoes dataset'}


api.add_namespace(predict, path='')
