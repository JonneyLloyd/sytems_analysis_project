from flask import request
from app import app, db
from app.models.user import User

@app.route('/')
def index():
    username = request.args.get('username')
    email = request.args.get('email')
    admin = User(username, email)
    db.session.add(admin)
    db.session.commit()
    return 'Hello %s\nThis is just an example. Visit 127.0.0.1:5000/?username=test&email=test@gmail.com to add a db entry. This code should reallt be in the api module rather than the controller' % username
