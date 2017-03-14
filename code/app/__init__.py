import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Load configuration
# TODO: extract to config file
app.secret_key = os.urandom(12)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/db_hotel'

# Set up DB
db = SQLAlchemy(app)

from app.controllers import frontend
from app.controllers import rest

# Initialise DB
db.create_all()
