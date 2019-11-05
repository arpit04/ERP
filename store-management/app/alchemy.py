from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ARPIT/projects/store-management/database.db'
db = SQLAlchemy(app)

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

class company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(80))
    address = db.Column(db.String(120))
    GST_number = db.Column(db.String(80))
    company_email = db.Column(db.String(80))
    contact = db.Column(db.String(80))

class finance(db.Model):
    __tablename__ = 'finance'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(80))
    start_date = db.Column(db.String(120))
    end_date = db.Column(db.String(80))
    finance_year = db.Column(db.String(80))

class items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    item_cat = db.Column(db.String(80))
    ITSN_code = db.Column(db.String(120))
    disc = db.Column(db.String(80))
    remark = db.Column(db.String(80))
    tax_type = db.Column(db.String(80))

class party(db.Model):
    __tablename__ = 'party'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address = db.Column(db.String(120))
    contact = db.Column(db.String(80))
    email = db.Column(db.String(80))
    firm_name = db.Column(db.String(80))
    GSTIN = db.Column(db.String(80))
    state = db.Column(db.String(80))
    state_code = db.Column(db.String(80))

class tax(db.Model):
    __tablename__ = 'tax'
    id = db.Column(db.Integer, primary_key=True)
    CGST = db.Column(db.String(80))
    SGST = db.Column(db.String(120))
    IGST = db.Column(db.String(80))
    CESS = db.Column(db.String(80))
    group_name = db.Column(db.String(80))

db.create_all()