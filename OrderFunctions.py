from flask import jsonify, request
from marshmallow import ValidationError

def get_order_tracking(order_id):
    from app import Orders, order_tracking_schema
    order = Orders.query.get(order_id)
    return order_tracking_schema.jsonify(order)

def get_order(order_id):
    from app import Orders, order_schema
    order = Orders.query.get(order_id)
    return order_schema.jsonify(order)

def add_order():
    from app import db, Orders, order_schema
    try:
        order_info = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400

    new_order = Orders(
        status = order_info['status']
        )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'New member added successfuly'}), 201

def update_order_tracking(order_id):
    from app import db, Orders, order_schema
    order = Orders.query.get_or_404(order_id)
    try:
        order_info = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages, 400)
    
    order.order_status = order_info['order_status']

    db.session.commit()
    return jsonify({'message': 'Order upated'}), 200

def void_order(order_id):
    from app import db, Orders
    order = Orders.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order voided'}), 200
 