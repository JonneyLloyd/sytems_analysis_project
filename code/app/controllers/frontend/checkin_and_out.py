from flask import render_template, redirect, url_for, request, session,flash
from flask import current_app as app

from app.api.user_manager import UserManager
from app.forms.checkin import CheckInForm,CheckOutForm
from app.api.CheckIn_and_Out import CheckInManager

@app.route('/checkin_and_out/surecheckin',methods=['GET','POST'])
def checkin():
    user_id = request.args.get('user_id')
    user = UserManager.get_user_by_id(user_id)
    bookings = CheckInManager.getBookingOB(user.first_name, user.last_name, user.credit_num)
    # TODO: check permissions
    if request.method == 'POST':
        var=int(request.form['r_num']);
        CheckInManager.change_avaliability(var)
        print('####', var, CheckInManager.get_Firstname())
        CheckInManager.update_Database(CheckInManager.get_Firstname(),CheckInManager.get_Lastname(),CheckInManager.get_CreditNum())
        return render_template('checkin_and_out/AcceptCheckIn.html', bookings=bookings, user=user)

@app.route('/checkin_and_out/checkinform',methods=['GET','POST'])
def verify():
    form=CheckInForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        credit_num = form.credit_num.data
        # form=CheckInManager.getForm();
        # form.Judge(fir, las, cre);

        bookings = CheckInManager.getBookingOB(first_name, last_name, credit_num)  # an attribute to record the judge result, if the user is valid.
        user = bookings[0].user

        if (len(bookings) > 0):
            leng = len(bookings);
            # CheckInManager.set_CreditNum(credit_num)
            # CheckInManager.set_Firstname(first_name)
            # CheckInManager.set_Lastname(last_name)
            # return render_template('checkin_and_out/AcceptCheckIn.html', bookings=bookings, user=user)
            print('#######redirect')
            redirect(url_for('checkin'))
            print('#######after')
            # redirect(url_for('checkin', user_id=user.id))
        else:
            flash('Sorry,the Name or CreditCard number is wrong or not bookings could be found\n', 'danger')
    return render_template('checkin_and_out/CheckIn.html',fm=form)

# @app.route('/checkin_and_out/checkinform',methods=['GET','POST'])
# def createForm():
#     form=CheckInForm();
#     # CheckInManager.setForm(form);
#     return render_template('checkin_and_out/CheckIn.html',fm=form)

@app.route('/checkin_and_out/checkoutform',methods=['GET','POST'])
def checkout():
    form=CheckOutForm();
    if request.method == 'POST':
        credit=request.form['credit_num'];
        if(form.Judge(credit)):
            print('Yes');
            return render_template('/checkin_and_out/AcceptCheckout.html')
        else:
            flash('Your credit card number is incorrect or you have no records to checkout','danger')
    return render_template('checkin_and_out/CheckOut.html',fm=form)
