from flask import render_template, redirect, url_for
from flask import current_app as app

from app.auth.login import UserIsNotAuthorized
from app.auth.access import UserIsNotPermitted


@app.errorhandler(UserIsNotAuthorized)
def user_not_authorised(error):
    return 'Unauthorised access. Please log in.', 403  # TODO: Add template


@app.errorhandler(UserIsNotPermitted)
def user_not_permitted(error):
    return 'Permission denied.', 403  # TODO: Add template


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404  # TODO: Add template
