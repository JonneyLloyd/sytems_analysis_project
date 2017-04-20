from flask import g, render_template, redirect, url_for, request, session, flash
from flask import current_app as app

from app.api.booking_view import BookingView
from app.api.room_manager import RoomManager
from app.forms.booking import BookingForm
from flask import render_template, redirect, url_for, request, session
from app.auth.login import LoginManager, login_required

from app.api.booking_manager import cancelBooking, makeBooking
from app.api.change_room_price import changePrice
from app.api.booking_manager import cancelBooking, makeBooking
from app.api.change_room_price import changePrice

@app.route('/booking/booking', methods=['GET', 'POST'])
@login_required
def booking():
    form = BookingForm()
    if form.validate_on_submit():
        result = BookingView.get_booking_for_user(g.user.id)
        if result:
            return render_template("booking/bookingView.html",result = result)

    return render_template('booking/bookingForm.html', form=form)

@app.route('/booking/bookingForm')
@login_required
def booking_view():
    return render_template('booking/bookingForm.html')


@app.route('/booking/booking', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        id = request.form['user_id']
        result = BookingView.get_booking_for_user(id)
        if result != False:
            return render_template("booking/bookingView.html", result=result)


@app.route('/accounts/make-book-form', methods=['GET', 'POST'])
def make_book_form():
    return render_template('booking/makebooking.html')


@app.route('/booking/cancelbookform', methods=['GET', 'POST'])
def cancel_booking_form():
    return render_template('booking/cancelBooking.html')


@app.route('/accounts/makebooking', methods=['GET', 'POST'])
def make_book():
    if request.method == 'POST':
        room_id = request.form['room_type']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        credit_card = request.form['credit_card']

    user_id = g.user.id
    success = False
    if credit_card != "" and start_date != "" and end_date != "" and room_id != "":
        success = makeBooking.bookingmake(user_id, room_id, start_date, end_date, credit_card)
    if (success):
        return render_template('booking/bookingSuccess.html')
    else:
        return render_template('booking/bookingFailed.html')


@app.route('/accounts/cancelbook', methods=['GET', 'POST'])
def cancel_booking():
    credit_card = request.form['credit_card']
    booked_room_number = request.form['booked_room_number']
    booked_start_date = request.form['booked_start_date']
    canceled = cancelBooking.bookingcancel(credit_card, booked_room_number, booked_start_date)
    if (canceled):
        return render_template('booking/roomCanceled.html')
    else:
        return render_template('booking/roomCancelFail.html')


@app.route('/booking/changepriceform', methods=['GET', 'POST'])
def change_price_form():
    return render_template('booking/changeprice.html')


@app.route('/accounts/changeprice', methods=['GET', 'POST'])
def change_price():
    if request.method == 'POST':
        room_id = request.form['room_id']
        weekday_price = request.form['weekday_price']
        weekend_price = request.form['weekend_price']

    user_id = g.user.id
    changePrice.pricechange(user_id, room_id, weekday_price, weekend_price)
    return render_template('booking/priceChanged.html')