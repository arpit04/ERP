from wtforms import Form, BooleanField, TextField, StringField, PasswordField, validators, IntegerField

class RegistrationForm(Form):
    company_name = TextField('company name',[validators.DataRequired("please enter company name"), validators.Length(min=2, max=35)])
    address = TextField('company Address', [validators.DataRequired("please enter company address"), validators.Length(min=2, max=35)])
    GST_number = TextField('GST number', [validators.DataRequired("please enter GST number")])
    company_email = TextField('Email Address', [validators.DataRequired("please enter email address"), validators.Length(min=2, max=35)])
    contact = TextField('contact number', [validators.DataRequired("please enter contact number"), validators.Length(min=2, max=10)])

class FinanceForm(Form):
    company_name = TextField('company_name', [validators.DataRequired("please enter company name")])
    start_date = TextField('Start Date', [validators.DataRequired("please enter start date")])
    end_date = TextField('End Date', [validators.DataRequired("please enter end date")])
    finance_year = TextField('Finance Year', [validators.DataRequired("please enter finance year")])

class ItemForm(Form):
    item_cat = TextField('Item Category', [validators.DataRequired("enter item category")])
    ITSN_code = IntegerField('Start Date', [validators.DataRequired("enter ITSN code")])
    disc = TextField('Discription', [validators.DataRequired("enter discription")])
    remark = TextField('Remark', [validators.DataRequired("enter remark")])
    tax_type = TextField('Tax Type', [validators.DataRequired("enter remark")])

class TaxForm(Form):
    CGST = TextField('CGST', [validators.DataRequired("enter CSGT")])
    SGST = TextField('SGST', [validators.DataRequired("enter SGST")])
    IGST = TextField('IGST', [validators.DataRequired("enter IGST")])
    CESS = TextField('CESS', [validators.DataRequired("enter CESS")])
    group_name = TextField('group_name', [validators.DataRequired("enter group_name")])

class PartyForm(Form):
    name = TextField('name', [validators.DataRequired("enter name")])
    address = TextField('address', [validators.DataRequired("enter address")])
    contact = TextField('contact', [validators.DataRequired("enter contact")])
    email = TextField('email', [validators.DataRequired("enter email")])
    firm_name = TextField('firm name', [validators.DataRequired("enter firm name")])
    GSTIN = TextField('GSTIN', [validators.DataRequired("enter GSTIN")])
    state = TextField('state', [validators.DataRequired("enter state")])
    state_code = TextField('state_code', [validators.DataRequired("enter state code")])