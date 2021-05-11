from app import db, Todo

db.drop_all()
db.create_all() # Creates all table classes defined


new_todo = Todo(task="added item to todo list",complete=0)

db.session.add(new_todo)
db.session.commit()