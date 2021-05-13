from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    all_todos = Todo.query.all()
    todos_string = ""
    for todo in all_todos:
        todos_string += "<br>" + str(todo.id) + todo.task + str(todo.complete) 
    return 'This is my TODO list'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.105.221.153:3306/flask_instance"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)

@app.route('/add')
def add():
    new_todo = Todo(task="New Todo", complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return "Added new Todo to list"

@app.route('/read')
def read():
    all_todo = Todo.query.all()
    todo_string = ""
    for todo in all_todo:
        todo_string += "<br>"+ todo.task
    return todo_string

if __name__=='__main__':
    app.run(debug=True, host='127.0.0.1')