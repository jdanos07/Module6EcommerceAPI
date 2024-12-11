from app import db, CustomerAccount, Customers, customer_schema, customers_schema, sch
from flask import request, jsonify
from marshmallow import ValidationError

def get_customers():
    customers = Customers.query.all()
    return customers_schema.jsonify(customers)

def get_customer(customer_id):
    customer = Customers.query.find_all(customer_id)
    return customer_schema.jsonify(customer)

def add_customer():
    try:
        customer_info = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400

    new_customer = Customers(
        customer_name = customer_info('customer_name'),
        email = customer_info('email'),
        phone = customer_info('phone')
        )
    
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'New member added successfuly'}), 201
 
def update_customer(customer_id):
    pass
    customer = Customers.query.get_or_404(customer_id)
    try:
        customer_info = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages, 400)
    
    customer.name=db.customer_info['name']
    customer.email=db.customer['email']
    customer.phone=db.customer['phone']

    db.session.commit()
    return jsonify({'message': 'Customer upated'}), 200

def delete_customer(customer_id): 
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Produc removed'}), 200

def get_customer_account(customer_id):
    pass
    # workouts = Workouts.query.all()
    # return workouts_schema.jsonify(workouts)

def add_customer_account():
    pass
    # try:
    #     workout_data = workout_schema.load(request.json)
    # except ValidationError as e:
    #     return jsonify(e.messages),400

    # new_workout = Workouts(
    #     calories_burned = workout_data['calories_burned'],
    #     duration_minutes = workout_data['duration_minutes'],
    #     date = workout_data['date']
    #     )
    # db.session.add(new_workout)
    # db.session.commit()
    # return jsonify({'message': 'New member added successfuly'}), 201
 
def update_customer_account(account_id):
    pass
    # workout = Workouts.query.get_or_404(member_id, workout_id)
    # try:
    #     workout_data = workout_schema.load(request.json)
    # except ValidationError as e:
    #     return jsonify(e.messages, 400)
    
    # workout.calories_burned = workout_data['calories_burned']
    # workout.duration_minutes = workout_data['duration_minutes']
    # workout.date = workout_data['date']

    # db.session.commit()
    # return jsonify({'message': 'Workout upated'}), 200

def delete_customer_account(customer_id):
    pass