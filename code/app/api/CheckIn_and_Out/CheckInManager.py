from app.extensions import db;
from app.models.booking import Booking
from app.models.user.user_details import UserDetails
from app.models.user import User
from app.models.room import Room
from app.models.room.room_price import RoomPrice
from app.models.role.role import Role
class CheckInManager(object):
    # @staticmethod
    # def set_Firstname(firstname):
    #     CheckInManager.first=firstname;
    # @staticmethod
    # def set_Lastname(lastname):
    #     CheckInManager.last = lastname;
    # @staticmethod
    # def set_CreditNum(creditnum):
    #     CheckInManager.credit=creditnum;
    # @staticmethod
    # def get_Firstname():
    #     return CheckInManager.first;
    # @staticmethod
    # def get_Lastname():
    #     return CheckInManager.last;
    # @staticmethod
    # def get_CreditNum():
    #     return CheckInManager.credit;
    # @staticmethod
    # def setForm(form):
    #     CheckInManager.form=form;
    # @staticmethod
    # def getForm():
    #     return CheckInManager.form;
    @staticmethod
    def getBookingOB(Firstname,Lastname,CreditNum):
        dbs=db.session.query(Booking).filter(UserDetails.id==User.id,Booking.user_id==User.id,UserDetails.first_name==Firstname,Booking.room_id==Room.id,Room.type==RoomPrice.id,UserDetails.last_name==Lastname,Booking.credit_card==CreditNum);
        if(dbs.first() is None):
            return []
        else:
            return dbs.all();
            # room_db = db.session.query(Room).filter(UserDetails.id == User.id, Booking.user_id == User.id,
            #                                         UserDetails.first_name == Firstname, Booking.room_id == Room.id,
            #                                         Room.type == RoomPrice.id,
            #                                         UserDetails.last_name == Lastname,
            #                                         Booking.credit_card == CreditNum);
        # return (lis,judge);

    @staticmethod
    def change_avaliability(room_num):
        s=db.session.query(Room).filter(Room.number==room_num).all();
        for m in s:
            m.availability ='N';
        db.session.commit();

    @staticmethod
    def update_Database(first,last,credit):
        dbs = db.session.query(Booking).filter(UserDetails.id == User.id, Booking.user_id == User.id,
                                               UserDetails.first_name == first, Booking.room_id == Room.id,
                                               Room.type == RoomPrice.id, UserDetails.last_name == last,
                                               Booking.credit_card == credit).all();
        CheckInManager.getForm().setlis(dbs);
