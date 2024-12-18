from flask import request, jsonify
from marshmallow import ValidationError

def get_customers():
    from app import Customers, customers_schema
    customers = Customers.query.all()
    return customers_schema.jsonify(customers)

def get_customer(customer_id):
    from app import Customers, customer_schema
    customer = Customers.query.get(customer_id)
    return customer_schema.jsonify(customer)

def add_customer():
    from app import db, CustomerAccount, Customers, customer_schema
    try:
        customer_info = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400

    new_customer = Customers(
        customer_name = customer_info('customer_name'),
        email = customer_info('email'),
        phone = customer_info('phone')
        )
    new_account = CustomerAccount()
    
    db.session.add(new_customer)
    db.session.add(new_account)
    db.session.commit()
    return jsonify({'message': 'New member added successfuly'}), 201
 
def update_customer(customer_id):
    from app import db, Customers, customer_schema
    from app import db, Customers, customer_schema
    customer = Customers.query.get_or_404(customer_id)
    try:
        customer_info = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages, 400)
    
    customer.name= customer_info['name']
    customer.email= customer_info['email']
    customer.phone= customer_info['phone']

    db.session.commit()
    return jsonify({'message': 'Customer upated'}), 200

def delete_customer(customer_id):
    from app import db, CustomerAccount, Customers 
    customer = Customers.query.get_or_404(customer_id)
    account = CustomerAccount.query.get_or_404(customer_id)
    db.session.delete(customer, account)
    db.session.commit()
    return jsonify({'message': 'Produc removed'}), 200

def get_customer_account(customer_id):
    from app import CustomerAccount, customer_acct_schema
    customer = CustomerAccount.query.get(customer_id)
    return customer_acct_schema.jsonify(customer)
