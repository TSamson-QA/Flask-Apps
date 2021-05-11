from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.105.221.153:3306/flask_instance"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float(10,2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    chosen_items = db.relationship("ChosenItems", backref="order") 

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(10,2), nullable=False)
    chosen_items = db.relationship("ChosenItems", backref="product")

class ChosenItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')