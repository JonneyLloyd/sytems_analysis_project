from flask import render_template, redirect, url_for, request, session
from flask import current_app as app
from flask import g, request, session, render_template, flash, redirect, url_for
from app.api.booking_view import BookingView
from app.api.booking_make import makeBooking
from app.api.booking_cancel import cancelBooking


@app.route('/booking/bookingForm')
def booking_view():
    return render_template('booking/bookingForm.html')


@app.route('/booking/booking', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        id = request.form['user_id']
        result = BookingView.get_booking_for_user(id)
        if result != False:
            return render_template("booking/bookingView.html", result=result)

@app.route('/accounts/make-book-form', methods=['GET','POST'])
def make_book_form():
   return render_template('booking/makebook.html')

@app.route('/booking/cancelbookform', methods=['GET','POST'])
def cancel_booking_form():

    return render_template('booking/cancelBooking.html')

@app.route('/accounts/makebook', methods=['GET','POST'])
def make_book():

    if request.method == 'POST':
        room_id = request.form['room_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        credit_card = request.form['credit_card']

    user_id = g.user.id
    makeBooking.bookingmake(user_id,room_id,start_date,end_date,credit_card)
    return "Thank you for you're booking  <a href="'/accounts/make-book-form'"> Book another room </a>"

@app.route('/accounts/cancelbook', methods=['GET','POST'])
def cancel_booking():
    credit_card = request.form['credit_card']
    canceled = cancelBooking.bookingcancel(credit_card)
    if(canceled):
        return "Your room has been canceled!"
    else:
        return "No matching booking was found <a href="'/booking/cancelbookform'"> Try Again? </a>"