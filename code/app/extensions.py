from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_nav import Nav

# Factories?
db = SQLAlchemy()
api = Api()
bootstrap = Bootstrap()
nav = Nav()
