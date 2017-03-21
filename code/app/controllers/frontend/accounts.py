from flask import g, request, session, render_template, flash, redirect, url_for
from flask import current_app as app

from app.auth.login import LoginManager, login_required
from app.auth.access import user_is, user_can
from app.forms.accounts import LoginForm, RegisterForm


@app.route('/accounts/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))

    return render_template('accounts/register.html', form=form)


@app.route('/accounts/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))

    return render_template('accounts/login.html', form=form)


@app.route("/accounts/logout")
def logout():
    LoginManager.logout()
    return redirect(url_for('home'))
