from flask import render_template, redirect, url_for
from flask import current_app as app

from app.auth.login import UserIsNotAuthorized
from app.auth.access import UserIsNotPermitted


@app.errorhandler(UserIsNotAuthorized)
def user_not_authorised(error):
    return render_template('accounts/permissionDenied.html'), 403
# <a href="/booking/cancelbookform"> Try Again? </a>


@app.errorhandler(UserIsNotPermitted)
def user_not_permitted(error):
    return render_template('accounts/permissionDenied.html'), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('accounts/noPage.html'), 404
