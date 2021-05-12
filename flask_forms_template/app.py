from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField, DecimalField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cvwfwiccnncwj'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = DateField("DOB", format='%d/%m/%Y')
    age = IntegerField("Age")
    salary = DecimalField("Salary", places=2)
    food = SelectField("Food", choices=[("Indian", "Indian"),("Pizza", "Pizza"),("Chinese", "Chinese")])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        if len(first_name) == 0 or len(last_name) == 0:
            error == "Please supply both first and last name"
        else:
            return f'thank_you {first_name} {last_name}, your date of birth is {dob}'
    
    return render_template('home.html', form=form, message=error)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')