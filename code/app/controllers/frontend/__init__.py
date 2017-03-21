# TODO: break this into separate controllers/.py files rather than in __inti__.py
from flask import g, request, session, render_template, flash, redirect, url_for
from app import app, db

from app.models.user import User
from app.models.role import Role
from app.models.room import Room
from app.models.booking import Booking
from app.models.permission import Permission

from app.auth.login import LoginManager, login_required, UserIsNotAuthorized
from app.auth.access import user_is, user_can, UserIsNotPermitted
from app.api.booking_view import Booking_view


@app.route('/accounts/register', methods=['GET'])
def register():
    if not LoginManager.is_logged_in():
        return render_template('accounts/register.html')
    else:
        return "Already registered!  <a href='/accounts/logout'>Logout</a>"


@app.route('/accounts/register', methods=['POST'])
def do_admin_register():
    email = request.form['email']
    password = request.form['password']
    # TODO: validation
    if LoginManager.register(email, password):
        return redirect(url_for('home'))

    flash('User exists already!', 'error')  # TODO: better errors
    return redirect(url_for('register'))


@app.route('/')
def home():
    if not LoginManager.is_logged_in():
        return "<h1>Home</h1>Hello!  <a href='/accounts/login'>Login</a>"
    else:
        return "<h1>Home</h1>Hello "+g.user.email+"!  <a href='/accounts/logout'>Logout</a>"


@app.route('/accounts/login', methods=['GET'])
def login():
    if not LoginManager.is_logged_in():
        return render_template('accounts/login.html')
    else:
        return "Already logged in!  <a href='/accounts/logout'>Logout</a>"


@app.route('/accounts/login', methods=['POST'])
def do_admin_login():
    email = request.form['email']
    password = request.form['password']

    if LoginManager.login(email, password):
        return redirect(url_for('home'))

    flash('wrong password!')  # TODO: better errors
    return redirect(url_for('login'))


@app.route("/accounts/logout")
def logout():
    LoginManager.logout()
    return redirect(url_for('home'))

@app.route('/booking/bookingForm')
def booking_view():
   return render_template('booking/bookingForm.html')

@app.route('/booking/booking',methods = ['POST','GET'])
def result():
      if request.method == 'POST':
      	id = request.form['user_id']
      	result = Booking_view.get_booking_for_user(id)
      	if result != False:
      		return render_template("booking/bookingView.html",result = result)


@app.before_request
def load_user():
    LoginManager.load_user()


@app.route("/private/special")
@login_required
def special():
    return 'So special... you must log in!'


@app.route("/private/admin")
@login_required
@user_is('ADMIN')
def special_admin():
    return 'Admin page'


@app.route("/private/guest")
@user_is('GUEST')
def special_guest():
    return 'Guest page'


@app.errorhandler(UserIsNotAuthorized)
def user_not_authorised(error):
    return 'Unauthorised access. Please log in.', 403  # TODO: Add template


@app.errorhandler(UserIsNotPermitted)
def user_not_permitted(error):
    return 'Permission denied.', 403  # TODO: Add template


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404  # TODO: Add template

