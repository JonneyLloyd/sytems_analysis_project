from app.extensions import db;
from app.models.booking import Booking
from app.models.user.user_details import UserDetails
from app.models.user import User
from app.models.room import Room
from app.models.room.room_price import RoomPrice
from app.models.role.role import Role
from flask import session
from sqlalchemy.ext.hybrid import hybrid_property
from flask import request,render_template
from flask_wtf import FlaskForm as Form
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import InputRequired
from app.api.CheckIn_and_Out.CheckInManager import CheckInManager
from app.api.CheckIn_and_Out.CheckOutManager import CheckOutManager
class CheckIn(Form):
    def _init_(self):
        self._lis=[];
    def setlis(self,lis):
        self._lis=lis;
    first_name=StringField('Firstname',validators=[InputRequired()])
    last_name=StringField('Lastname',validators=[InputRequired()])
    credit_num=IntegerField('Credit',validators=[InputRequired()])
    submit=SubmitField('Submit')
    def Judge(self,first_name,last_name,credit_num):
        result=CheckInManager.getBookingOB(first_name,last_name,credit_num);
        self.judge=result[1];#an attribute to record the judge result, if the user is valid.
        self._lis=result[0];
    def getBookingOb(self):
        return self._lis
    def chu(self):
        print("I was clicked!");
class CheckOut(Form):
    credit_num = StringField('CreditNum', validators=[InputRequired()])
    def Judge(self,credit_num):
        return CheckOutManager.Judge(credit_num);