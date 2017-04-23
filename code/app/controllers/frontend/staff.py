from flask import g, render_template, redirect, url_for, request, session, flash
from flask import current_app as app
from app.extensions import db
from app.api.user_manager import UserManager
from flask import render_template, redirect, url_for, request, session
from app.models.user import User
from app.forms.accounts import LoginForm, RegisterForm, ProfileForm, RegisterFormStaff
import datetime

@app.route('/staff/add_staff', methods=['GET', 'POST'])
# @login_required
def add_staff():

    if request.method == 'POST':
        email = request.form['email']
        role = request.form['role']
        password = request.form['password']

    UserManager.create_staff(email,password,role)
    return render_template('staff/staff_updated.html',page=1)


@app.route('/staff/add_staff_form', methods=['GET', 'POST'])
# @login_required
def add_staff_form():
    form = RegisterFormStaff()

    return render_template('staff/add_staff.html', form=form)

@app.route('/staff/remove_staff', methods=['GET', 'POST'])
# @login_required
def remove_staff():

    if request.method == 'POST':
        email = request.form['staff_email']
        role = request.form['staff_role_id']
        staff_id = request.form['staff_id']

    UserManager.remove_staff(email, staff_id, role)
    return render_template('staff/staff_updated.html', page=2)


@app.route('/staff/remove_staff_form', methods=['GET', 'POST'])
# @login_required
def remove_staff_form():
    this_user = g.user.id
    staff_list = User.query.filter(User._role_id !=1, User.id != this_user).all()


    return render_template('staff/remove_staff.html', staff_list = staff_list)