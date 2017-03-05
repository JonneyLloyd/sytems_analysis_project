from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/db_hotel'
db = SQLAlchemy(app)

from app.controllers import frontend

db.create_all()
