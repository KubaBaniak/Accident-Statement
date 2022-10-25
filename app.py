from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TelField, DateField, TimeField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Regexp
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "5ae4aab58e1760eb305948786be1ad3fb30fac226e5c897edee395ab7022f51a"

class MyForm(FlaskForm):
    full_name = StringField('Full name', [DataRequired()])
    address = StringField('Address', [DataRequired()])
    phone_number = TelField('Phone number', [DataRequired(), Length(max=9, message="Please enter a phone number in this format 123456789"), Regexp("^[0-9]")])
    driving_license_cat = SelectField('Driving license category', choices=['AM', 'A1', 'A2', 'A', 'B1', 'B', 'C1', 'C', 'D1', 'D', 'BE', 'C1E', 'CE', 'D1E', 'DE', 'T'])
    id_number = StringField("ID number", [DataRequired(), Regexp("^(?=.*[-+_!@#$%^&*., ?])", message="No special characters allowed")])
    id_provider = StringField("ID Provider")
    date = DateField("Date of an accident")
    hour = TimeField("Time of an accident")
    location = StringField('Location of accident', [DataRequired()])
    street = StringField('Street', [DataRequired()])
    car = StringField('Car brand', [DataRequired()])
    license_plate = StringField('License plate', [DataRequired()])
    car_owner = StringField('Cars owner', [DataRequired()])
    insurance_company = StringField('Insurance company')
    policy_id = StringField('Policy id number')
    expiry_date = DateField("Policy expiry date")
    victims_name = StringField('Victims name', [DataRequired()])
    victims_car = StringField('Victims car', [DataRequired()])
    victims_license_plate = StringField('Victims license plate', [DataRequired()])
    accident_description = TextAreaField('Accident description')
    victims_car_damage = TextAreaField('Victims car damage description')
    perpetrator_car_damage = TextAreaField('Perpetrator car damage description')
    other_damage = TextAreaField('Other damage description')
    witnesses_names = TextAreaField('Witnesses (seperate with /)')
    


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/form")
def form():
    form = MyForm()
    if form.validate_on_submit():
        redirect(url_for('index'))
    return render_template("form.html", form=form)
