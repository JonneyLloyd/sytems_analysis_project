from flask import g, render_template, redirect, url_for, request, session, flash
from flask import current_app as app
from app.extensions import db
from app.api.booking_view import BookingView
from app.api.room_manager import RoomManager
from app.forms.booking import BookingForm
from flask import render_template, redirect, url_for, request, session
from app.api.booking_manager import cancelBooking, makeBooking
from app.models.room import Room,RoomPrice
from app.models.booking import Booking
from app.auth.login import LoginManager,login_required
from app.auth.access import user_is, user_can

@app.route('/booking/booking', methods=['GET', 'POST'])
@login_required
def booking():
    form = BookingForm()
    if form.validate_on_submit():
        result = BookingView.get_booking_for_user(g.user.id)
        if result:
            return render_template("booking/bookingView.html", result=result)


    return render_template('booking/bookingForm.html', form=form)

@app.route('/booking/bookingForm')
@login_required
def booking_view():
    return render_template('booking/bookingForm.html')


@app.route('/booking/booking', methods=['POST', 'GET'])
@login_required
def result():
    if request.method == 'POST':
        id = request.form['user_id']
        result = BookingView.get_booking_for_user(id)
        if result != False:
            return render_template("booking/bookingView.html", result=result)


@app.route('/accounts/make-book-form', methods=['GET', 'POST'])
@login_required
def make_book_form():

    room_list = get_existing_rooms()

    return render_template('booking/makebooking.html', room_list = room_list)


@app.route('/booking/cancelbookform', methods=['GET', 'POST'])
@login_required
def cancel_booking_form():
    user_id = g.user.id
    customer_bookings = Booking.query.filter_by(user_id = user_id).all()
    print(customer_bookings)

    bookings_start = []
    bookings_room = []
    bookings_price = []
    bookings_card = []
    for book in customer_bookings:
        bookings_start.append(book.start_date)
        bookings_room.append(book.room_id)
        bookings_price.append(book.booking_price)
        bookings_card.append(book.credit_card)

    return render_template('booking/cancelBooking.html', bookings = bookings_start,bookings2 =bookings_room )


@app.route('/accounts/makebooking', methods=['GET', 'POST'])
@login_required
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
@login_required
def cancel_booking():
    credit_card = request.form['credit_card']
    booked_room_number = request.form['booked_room_number']
    booked_start_date = request.form['booked_start_date']
    print(booked_start_date)
    user_id = g.user.id
    canceled = cancelBooking.bookingcancel(user_id,credit_card, booked_room_number, booked_start_date)
    if (canceled):
        return render_template('booking/roomCanceled.html')
    else:
        return render_template('booking/roomCancelFail.html')


@app.route('/booking/changepriceform', methods=['GET', 'POST'])
@user_is('ADMIN')
def change_price_form():

    room_list = get_existing_rooms()

    return render_template('booking/changeprice.html', room_list=room_list)


@app.route('/accounts/changeprice', methods=['GET', 'POST'])
def change_price():
    if request.method == 'POST':
        room_id = request.form['room_id']
        weekday_price = request.form['weekday_price']
        weekend_price = request.form['weekend_price']

    return render_template('booking/priceChanged.html')


def get_existing_rooms():

    room_list =[]
    room_list2 =[]

    for value in db.session.query(Room.type).distinct():
        room_list.append(value)

    for room_value in room_list:
        name = RoomPrice.query.filter_by(id=room_value[0]).first()
        name2 = name.type
        room_list2.append(name2)

    return room_list2