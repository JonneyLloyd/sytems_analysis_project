from flask import render_template, redirect, url_for, request, session
from flask import current_app as app

from app.api.booking_view import Booking_view

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
