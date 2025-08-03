from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    # Exercise:
    # add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
    # make coffee/wifi/power a select element with choice of 0 to 5.
    #e.g. You could use emojis ☕️/💪/✘/🔌
    # make all fields required except submit
    # use a validator to check that the URL field has a URL entered.
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["0", "1", "2", "3", "4", "5"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["0", "1", "2", "3", "4", "5"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["0", "1", "2", "3", "4", "5"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        coffee = "☕" * int(form.coffee_rating.data) if form.coffee_rating.data != "0" else "✘"
        wifi = "💪" * int(form.wifi_rating.data) if form.wifi_rating.data != "0" else "✘"
        power = "🔌" * int(form.power_rating.data) if form.power_rating.data != "0" else "✘"
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{coffee},"
                           f"{wifi},"
                           f"{power}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
