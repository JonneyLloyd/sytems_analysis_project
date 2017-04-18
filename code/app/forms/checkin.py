from flask_wtf import FlaskForm as Form
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import Required
from app.api.CheckIn_and_Out.CheckInManager import CheckInManager
from app.api.CheckIn_and_Out.CheckOutManager import CheckOutManager


class CheckInForm(Form):
    # def _init_(self):
    #     self._lis=[];
    # def setlis(self,lis):
    #     self._lis=lis;
    first_name=StringField('Firstname', [Required()])
    last_name=StringField('Lastname', [Required()])
    credit_num=IntegerField('Credit', [Required()])
    # submit=SubmitField('Submit')
    # def Judge(self,first_name,last_name,credit_num):
    #     result=CheckInManager.getBookingOB(first_name,last_name,credit_num);
    #     self.judge=result[1];#an attribute to record the judge result, if the user is valid.
    #     self._lis=result[0];
    # def getBookingOb(self):
    #     return self._lis
    # def chu(self):
    #     print("I was clicked!");


class CheckOutForm(Form):
    credit_num = StringField('CreditNum', [Required()])
    def Judge(self,credit_num):
        return CheckOutManager.check_out(credit_num);