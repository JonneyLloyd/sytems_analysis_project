from app.models.room import Room
from app.models.room import RoomPrice
from app.extensions import db
from app.models.booking import Booking
from app.api.room_manager import RoomManager
from app.models.room import RoomStatus
from datetime import datetime, date, timedelta
import datetime


class manageStaff(object):
    @staticmethod
    def add_staff():
        print("TEST IS ENTERING HERE")
