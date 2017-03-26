from flask import render_template, redirect, url_for, request, session
from flask import current_app as app

from app.api.booking_view import BookingView
from app.api.room_manager import RoomManager

@app.route('/booking/bookingForm')
def booking_view():
   return render_template('booking/bookingForm.html')

@app.route('/booking/booking',methods = ['POST','GET'])
def result():
      if request.method == 'POST':
      	id = request.form['user_id']
      	result = BookingView.get_booking_for_user(id)
      	if result != False:
      		return render_template("booking/bookingView.html",result = result)

'''
Quick test for sales and room manager. Will remove
print "/nTEST"
print BookingView.view_sales_between_dates("2015-01-01", "2017-01-01")
print "END TEST/n"

print "/nTEST"
print RoomManager.get_room_price_from_type('single')
print "END TEST/n"

print "/nTEST"
print RoomManager.get_room_price_from_number(101)
print "END TEST/n"

print "/nTEST"
print RoomManager.get_room(101)
print "END TEST/n"
'''
