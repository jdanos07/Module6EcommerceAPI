from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from CustomerFunctions import get_customer, get_customers, get_customer_account, add_customer, update_customer_account, update_customer, delete_customer
from OrderFunctions import get_order, get_order_tracking, add_order
from ProductFunctions import get_product, get_products, get_product_list, add_product, update_product, delete_product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:J!strM3str@localhost/ecommerce_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class CustomerSchema(ma.Schema):
    customer_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone_number = fields.Str(required=True)

    class Meta:
        fields = ('customer_name', 'email', 'phone','customer_id')

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

class ProductSchema(ma.Schema):
    product_name = fields.Str(required=True)
    product_price = fields.Str(required=True)

    class Meta:
        fields = ('product_name', 'product_price', 'product_id')

product_schema = ProductSchema()
products_schema = ProductSchema (many=True)

class CustomerAcctSchema(ma.Schema):
    class Meta:
        fields = ('account_id', 'customer_id', 'orders')

customer_acct_schema = CustomerAcctSchema()
 
class Customers(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(2), nullable=False)
    HOLDER = db.relationship('', backref='')

class CustomerAccount(db.Model):
    __tablename__ = 'customer_account'
    account_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer_orders = db.relationship('Orders', backref=('customer_account'))

class Products(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(11), nullable=False)
    product_price = db.Column(db.String(5), nullable=False)

class Orders(db.Model):
    __tablename__ = 'orders'
    status = ''
    customer_id = ''
    product_id = ''
    order_id = '' 


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return "E-Commerce Management Database"

@app.route('/customers', methods=['GET'])
def app_get_customers():
    return get_customers
@app.route('/customers', methods=['PUT'])
def app_add_customer():
    return add_customer
@app.route('/customers/<int:id>', methods=['GET'])
def app_get_customer():
    return get_customer
@app.route('/customers/<int:id>', methods=['DEL'])
def app_delete_customer():
    return delete_customer()
@app.route('/customers/<int:id>', methods=['POST'])
def app_update_customer():
    return update_customer

@app.route('/customeraccount/<int:id>', methods=['POST'] )
def app_update_customer_account():
    return update_customer_account
@app.route('/customeraccount/<int:id>')
def app_get_customer_account():
    return get_customer_account()


@app.route('/products')
def app_get_products():
    return get_products()
@app.route('/products')
def app_add_product():
    return add_product
@app.route('/products/<int:id>')
def app_update_product():
    return update_product()
@app.route('/products/<int:id>')
def app_get_product():
    return get_product()
@app.route('/products/<int:id>')
def app_delete_product():
    return delete_product()
@app.route('/products_list')
def app_product_list():
    return get_product_list()

@app.route('/orders')
def app_add_order():
    return add_order()
@app.route('/orders/<int:id>')
def app_get_order():
    return get_order()
@app.route('/orders/<int:id>')
def app_get_order_tracking():
    return get_order_tracking()

if __name__ == '__main__':
    app.run(debug=True)
