from flask import render_template, redirect, url_for, request, session
from flask import current_app as app

from app.api.room_manager import RoomManager
from app.forms.rooms import RoomAvailabilityForm

@app.route('/rooms/rooms', methods=['GET', 'POST'])
def rooms():
    form = RoomAvailabilityForm()
    if form.validate_on_submit():
        result = RoomManager.get_rooms_occupied_on_date(date=form.date.data, room_type=form.room_type.data)
        return render_template("rooms/roomview.html",result = result)

    return render_template('rooms/rooms.html', form=form)
