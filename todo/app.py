from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.105.221.153:3306/flask_instance"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "dnidfbbjfl"

db = SQLAlchemy(app) 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)

class TodoForm(FlaskForm):
    task = StringField("Task")
    submit = SubmitField("Submit")

@app.route('/')
@app.route('/home')
def index():
    all_todos = Todo.query.all()
     
    return render_template("index.html", all_todos=all_todos)

@app.route('/add', methods=["GET", "POST"])
def add():
    form = TodoForm()
    if form.validate_on_submit():

        new_todo = Todo(task=form.task.data, complete=False)
        db.session.add(new_todo)
        db.session.commit()
    return render_template("add.html", form=form)

@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.complete = True
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/incomplete/<int:todo_id>")
def incomplete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.complete = False
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__=='__main__':
    app.run(debug=True, host='127.0.0.1')