from flask import g, session
from app import db
from app.models.user import User
from app.models.role import RoleEnum


class LoginManager(object):  # should login and user be separate models??

    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(password):
            return False  # exception??

        session['logged_in'] = True
        session['user_id'] = user.id
        g.user = user
        return True

    @staticmethod
    def logout():
        session['logged_in'] = False
        session.pop('user_id', None)

    @staticmethod                   # Separate class/module?
    def register(email, password):  # validation should have already been done?
        if User.query.filter_by(email=email).first():
            # flash('User exists already!')
            return False  # exception??

        user = User(email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        LoginManager.login(email, password)
        return True

    @staticmethod
    def load_user():
        if "user_id" in session:
            user = User.query.filter_by(id=session["user_id"]).first()
            session['logged_in'] = True
        else:
            user = User(None)  # Anonymous User instead? TODO: how to track the user session without a user_id
            user.set_role(RoleEnum.ANONYMOUS)
            session['logged_in'] = False
        g.user = user

    @staticmethod
    def get_current_user():
        return g.user

    @staticmethod
    def is_logged_in():
        return session['logged_in']
