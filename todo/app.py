from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is my TODO list'




app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.105.221.153:3306/flask_instance"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)

#WIP adding Todo page
@app.route('/todo')
def todo():
    all_todo = Todo.query.all()
    return str(all_todo[0].task)
    #find way to print/return entries from table?

if __name__=='__main__':
    app.run(debug=True, host='127.0.0.1')