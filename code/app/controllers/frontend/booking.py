from flask import render_template, redirect, url_for, request, session
from flask import current_app as app

from app.api.booking_view import BookingView
from app.api.room_manager import RoomManager
from app.forms.booking import BookingForm

@app.route('/booking/booking', methods=['GET', 'POST'])
def booking():
    form = BookingForm()
    if form.validate_on_submit():
        result = BookingView.get_booking_for_user(user_id=form.user_id.data)
        return render_template("booking/bookingView.html",result = result)

    return render_template('booking/bookingForm.html', form=form)

'''
Quick test for sales and room manager. Will remove
'''


'''

print "\nTEST get_rooms_occupied_on_date"

print RoomManager.get_rooms_occupied_on_date("2017-01-01", 1)
print "END TEST\n"

RoomManager.set_availability_for_booking("2017-01-01", 1)
RoomManager.set_availability_for_booking("2017-01-01", 1)
RoomManager.set_availability_for_booking("2017-01-01", 1)
RoomManager.set_availability_for_booking("2017-01-01", 1)

print "\nTEST get_rooms after decrease"
print RoomManager.get_rooms_occupied_on_date("2017-01-01", 1)
print "END TEST\n"

print "\nTEST increase booking"
RoomManager.increase_availability_for_booking("2017-01-01", 1)
RoomManager.increase_availability_for_booking("2017-01-01", 1)
RoomManager.increase_availability_for_booking("2017-01-01", 1)
RoomManager.increase_availability_for_booking("2017-01-01", 1)

print RoomManager.get_rooms_occupied_on_date("2017-01-01", 1)
print "END TEST\n"

print "\nTEST"
print RoomManager.get_room_price_from_type('single')
print "END TEST\n"

print "\nTEST"
print RoomManager.get_room_price_from_number(101)
print "END TEST\n"

print "\nTEST"
print RoomManager.get_room(101)
print "END TEST\n"

print "\nTEST"
print RoomManager.get_room_availablity(101)
print "END TEST\n"

print "\nTEST"
print RoomManager.get_room_clean(101)
print "END TEST\n"

print "\nTEST"
print RoomManager.set_room_availablity(101, 'on fire')
print "END TEST\n"

print "\nTEST"
print RoomManager.set_room_clean(101,  False)
print "END TEST\n"

print "\nTEST"
print RoomManager.get_room_availablity(101)
print "END TEST\n"

print "\nTEST"
print RoomManager.get_room_clean(101)
print "END TEST\n"

'''
