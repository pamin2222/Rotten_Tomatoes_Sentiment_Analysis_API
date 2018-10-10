from flask import Flask
from api import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11005, debug=True)
