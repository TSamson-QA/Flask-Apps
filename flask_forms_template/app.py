from datetime import datetime
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date = DateField('Date')
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date = form.date.data
        if len(first_name) == 0 or len(last_name) == 0:
            error == "Please supply both first and last name"
        else:
            return 'thank_you ' + first_name  + " " + last_name + " " + str(date)
    
    return render_template('home.html', form=form, message=error)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')