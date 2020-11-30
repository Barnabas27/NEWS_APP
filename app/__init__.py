from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    
    return app
# app = Flask(__name__,instance_relative_config = True)

# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')
# bootstrap = Bootstrap(app)
# from app import views