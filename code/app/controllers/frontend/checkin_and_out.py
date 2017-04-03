from flask import render_template, redirect, url_for, request, session,flash
from flask import current_app as app
from app.forms.Checkin_and_out import CheckIn,CheckOut
from app.api.CheckIn_and_Out import CheckInManager
'''
@app.route('/checkin_and_out/checkinform',methods=['GET','POST'])
def checkin():
    form = CheckIn();
    if request.method == 'GET' and request.args.get('checkin_id'):
        return request.args.get('checkin_id');
    if request.method == 'POST':
        fir = request.form['first_name'];
        las = request.form['last_name'];
        cre = request.form['credit_num'];
        form.Judge(fir,las,cre);
        if(form.judge):
            leng=len(form.getBookingOb());
            return render_template('checkin_and_out/AcceptCheckIn.html',fm=form,first=fir,last=las,leng=leng);
        else:
            flash('Sorry,the Name or CreditCard number is wrong\n','danger');
    return render_template('checkin_and_out/CheckIn.html',fm=form);
'''
@app.route('/checkin_and_out/surecheckin',methods=['GET','POST'])
def checkin():
    if request.method == 'POST':
#        print("I was invoked hjhhj!");
        var=int(request.form['r_num']);
        CheckInManager.change_avaliability(var)
        CheckInManager.update_Database(CheckInManager.get_Firstname(),CheckInManager.get_Lastname(),CheckInManager.get_CreditNum())
        form=CheckInManager.getForm();
        return render_template('checkin_and_out/AcceptCheckIn.html',fm=form)

@app.route('/checkin_and_out/verifyform',methods=['GET','POST'])
def verify():
    if request.method == 'POST':
        fir = request.form['first_name'];
        las = request.form['last_name'];
        cre = request.form['credit_num'];
        form=CheckInManager.getForm();
        form.Judge(fir, las, cre);
        if (form.judge is True):
            leng = len(form.getBookingOb());
            CheckInManager.set_CreditNum(cre)
            CheckInManager.set_Firstname(fir)
            CheckInManager.set_Lastname(las)
            return render_template('checkin_and_out/AcceptCheckIn.html', fm=form);
        else:
            flash('Sorry,the Name or CreditCard number is wrong\n', 'danger');
    return render_template('checkin_and_out/CheckIn.html',fm=form)

@app.route('/checkin_and_out/checkinform',methods=['GET','POST'])
def createForm():
    form=CheckIn();
    CheckInManager.setForm(form);
    return render_template('checkin_and_out/CheckIn.html',fm=form);

@app.route('/checkin_and_out/checkoutform',methods=['GET','POST'])
def checkout():
    form=CheckOut();
    if request.method == 'POST':
        credit=request.form['credit_num'];
        if(form.Judge(credit)):
            print('Yes');
            return render_template('/checkin_and_out/AcceptCheckout.html')
        else:
            flash('Your credit card number is incorrect or you have no records to checkout','danger')
    #if request.method == 'POST'
    return render_template('checkin_and_out/CheckOut.html',fm=form)
