from app.app_factory import AppFactory
from app.extensions import db
from config import TestConfig


from datetime import datetime

from app.api.booking_view import BookingView
from app.api.room_manager import RoomManager
from app.api.user_manager import UserManager
from app.models.user import User
from app.models.user import UserDetails
from app.models.room import RoomPrice
from app.models.room import Room
from app.models.booking import Booking
from app.api.booking_manager import cancelBooking, makeBooking
import datetime
from app.api.utils import Observable
from app.api.utils import Observer
from app.api.utils import ObserverTest


class TestBookingManger:
    @classmethod
    def setup_class(cls):
        cls.app = AppFactory.create_app(TestConfig)
        # db.init_app(cls.app)

        with cls.app.app_context():
            db.create_all()
            roomPrice = RoomPrice("single", 100, 150)
            room = Room(1, 101, 3, "Available", 1)
            # booking = Booking(1, 1, datetime.datetime.strptime('2017-01-02', '%Y-%m-%d').date()
            # ,datetime.datetime.strptime('2017-01-10', '%Y-%m-%d').date(), 123123123, 2000)
            booking = Booking(1, 101, datetime.datetime.strptime('2017-01-02', '%Y-%m-%d').date()
                              , datetime.datetime.strptime('2017-01-10', '%Y-%m-%d').date(), 123123123, 2000)
            RoomManager.set_availability_for_booking(datetime.datetime.strptime("2017-01-01", '%Y-%m-%d').date(), 1)

            UserManager.create_user("asd@asd.asd", "asdasd")
            user = UserManager.get_user("asd@asd.asd")
            UserManager.update_details(user, "mr", "test", '05644654')

            db.session.add(roomPrice)
            db.session.add(room)
            db.session.add(booking)
            db.session.commit()

        print ("Starting booking view tests")

    @classmethod
    def teardown_class(cls):
        print ("Ending booking view tests")
        with cls.app.app_context():
            db.drop_all()

    def setup(self):
        print ("Runs before each test method")

    def teardown(self):
        print ("Runs after each test method")

    def bookingmake_test(self):
        with self.app.app_context():
            result = makeBooking.bookingmake(1, 1, '2017-07-24', '2017-07-25', 1234)
            assert result != False


    def pricechange_test(self):
        with self.app.app_context():
            result = RoomManager.pricechange(1,1235,4565)
            assert result != False

    def bookingcancel_test(self):
        with self.app.app_context():

            result = cancelBooking.bookingcancel(1, 123123123, 101, '20170102')
            assert result != False





