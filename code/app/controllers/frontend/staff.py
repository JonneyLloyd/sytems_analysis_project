from flask import g, render_template, redirect, url_for, request, session, flash
from flask import current_app as app
from app.extensions import db
from app.api.booking_view import BookingView
from app.api.staff_manager import manageStaff
from app.api.user_manager import UserManager
from app.forms.booking import BookingForm
from flask import render_template, redirect, url_for, request, session
from app.api.booking_manager import cancelBooking, makeBooking
from app.models.room import Room,RoomPrice
from app.models.booking import Booking
from app.auth.login import LoginManager,login_required
from app.auth.access import user_is, user_can
from app.forms.accounts import LoginForm, RegisterForm, ProfileForm, RegisterFormStaff
import datetime

@app.route('/staff/add_staff', methods=['GET', 'POST'])
# @login_required
def add_staff():

    if request.method == 'POST':
        email = request.form['email']
        role = request.form['role']
        password = request.form['password']


    manageStaff.add_staff()
    UserManager.create_staff(email,password,role)


    return render_template('staff/staff_added.html')


@app.route('/staff/add_staff_form', methods=['GET', 'POST'])
# @login_required
def add_staff_form():
    form = RegisterFormStaff()

    return render_template('staff/add_staff.html', form=form)