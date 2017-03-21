# TODO: break this into separate controllers/.py files rather than in __inti__.py
import types
from flask import g, request, abort, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from flask import current_app as app
from app.extensions import db, api

from app.models.user import User

from app.auth.login import LoginManager

basic_auth = HTTPBasicAuth()


def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)


# @api.route('/users/<username>')   # api may be better than app if we set different functions for delete, post, get, etc
# class User(Resource):
#     def get(self, username):
#         return {'username': username}


@app.route('/api/users/register', methods=['POST'])
def api_register():
    email = request.json.get('email')
    password = request.json.get('password')  # TODO: validate
    if not LoginManager.register(email, password):
        abort(400)  # existing user/error
    return (jsonify({'email': g.user.email}),
            201
            # {'Location': url_for('get_user', id = user.id, _external = True)}     # Suggest location of next request
            )


@app.route('/api/resource')
@basic_auth.login_required
def api_get_protected_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.email})


@basic_auth.verify_password
def api_verify_password(email, password):
    return LoginManager.login(email, password)
