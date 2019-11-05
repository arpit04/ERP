from app import app
from flask import Flask, render_template, request, redirect, make_response,jsonify, send_from_directory, abort, url_for, flash, session, url_for, logging
import datetime
import requests
import os
# import jwt
from werkzeug.utils import secure_filename
import random
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from app.alchemy import user, company, finance, items, party, tax
from app.forms import RegistrationForm, FinanceForm, ItemForm, TaxForm, PartyForm
from functools import wraps
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity,set_access_cookies
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ARPIT/projects/store-management/database.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'secret'
jwt = JWTManager(app)
app.config['JWT_TOKEN_LOCATION']= 'cookies'


@app.route("/",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # req = request.values
        # uname = req["username"]
        # passw = req["password"]
        uname = request.form["uname"]
        # session['username'] = request.form["uname"]
        passw = request.form["passw"]
        users = user.query.filter_by(username=uname).all()
        for us in users:
            pass
        if not users:
            return jsonify({"message":"user not found"})
        if check_password_hash(us.password,passw): 
            jwt = create_access_token(identity=us.username)
            
            # headers = {'headers':jwt}
            resp = redirect(url_for('protected'))
            # requests.post('http://127.0.0.1:5000')
            set_access_cookies(resp, jwt)   #access cookie and verify jwt token
            return resp
        return render_template("public/login.html")
    return render_template("public/login.html")
# @app.route('/re')
# def re():
#     username = "admin"
#     email = "admin@mail.com"
#     password = generate_password_hash("abcde",method='sha256')
#     result = user(username=username,email=email,password=password)
#     db.session.add(result)
#     db.session.commit()
#     return "success"
@app.route('/register', methods=['GET', 'POST'])
def register():
    rows = company.query.order_by(company.company_name)
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        result = company(company_name=form.company_name.data, address=form.address.data, GST_number=form.GST_number.data, company_email=form.company_email.data, contact=form.contact.data)
        db.session.add(result)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('register'))
    return render_template('public/companies.html',rows=rows, form=form)

@app.route("/fin", methods=['GET', 'POST'])
def fin():
    row = finance.query.filter_by(company_name=session['Company'])
    cname = session['Company']
    form = FinanceForm(request.form)
    if request.method == 'POST' and form.validate():
        result = finance(company_name=cname, start_date=form.start_date.data, end_date=form.end_date.data, finance_year=form.finance_year.data)
        db.session.add(result)
        db.session.commit()
        return redirect(url_for('fin'))
    return render_template('public/welcome.html', row=row, form=form)

@app.route('/finyear', methods=['GET','POST'])
def finyear():
    if request.method == 'POST':
        # flash('message for welcome company page')
        session['Company'] = request.form["companies"]
        return redirect(url_for('fin'))
    return render_template('public/welcome.html', row=row)

@app.route('/task', methods=['GET','POST'])
def task():
    if request.method == 'POST':
        session['year'] = request.form["finyear"]
        return redirect(url_for('Item'))
    return render_template('public/dashboard.html')

@app.route('/Item', methods=['GET','POST'])
def Item():
    form = ItemForm(request.form)
    # flash('message for item master')
    if request.method == 'POST' and form.validate():
        result = items(item_cat=form.item_cat.data, ITSN_code=form.ITSN_code.data, disc=form.disc.data, remark=form.remark.data, tax_type=form.tax_type.data)
        db.session.add(result)
        db.session.commit()
        return render_template('public/Item-Master.html', form=form)
    return render_template('public/Item-Master.html', form=form)

@app.route('/Tax', methods=['GET','POST'])
def Tax():
    form = TaxForm(request.form)
    if request.method == 'POST' and form.validate():
        result = tax(CGST=form.CGST.data, SGST=form.SGST.data, IGST=form.IGST.data, CESS=form.CESS.data, group_name=form.group_name.data)
        db.session.add(result)
        db.session.commit()
        return render_template('public/Tax-Master.html', form=form)
    return render_template('public/Tax-Master.html', form=form)

@app.route('/Party', methods=['GET','POST'])
def Party():
    form = PartyForm(request.form)
    print()
    if request.method == 'POST' and form.validate():
        result = party(name=form.name.data, address=form.address.data, contact=form.contact.data, email=form.email.data
        , firm_name=form.firm_name.data, GSTIN=form.GSTIN.data, state=form.state.data, state_code=form.state_code.data)
        db.session.add(result)
        db.session.commit()
        return redirect(url_for('Party'))
    return render_template('public/Party-Master.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('you are logged out')
    return redirect(url_for('login'))
    
@app.route('/protected',methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    print("flask_jwt_extended verified")
    return jsonify(logged_in_as=current_user), 200