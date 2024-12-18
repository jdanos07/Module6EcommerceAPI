from flask import jsonify, request
from marshmallow import ValidationError

def get_products():
    from app import db, Products, products_schema
    products = Products.query.all()
    return products_schema.jsonify(products)

def get_product(product_id):
    from app import db, Products, product_schema
    product = Products.query.get(product_id)
    return product_schema.jsonify(product)

def add_product():
    from app import db, Products, product_schema
    try:
        product_info = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400

    new_product = Products(
        product_name = product_info['product_name'],
        product_price = product_info['product_price'],
        )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'New member added successfuly'}), 201
 
def update_product(product_id):
    from app import db, Products, product_schema
    product = Products.query.get_or_404(product_id)
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages, 400)
    
    product.name = product_data['product_name']
    product.price = product_data['product_price']

    db.session.commit()
    return jsonify({'message': 'Product upated'}), 200

def delete_product(product_id):
    from app import db, Products
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product removed'}), 200

def get_product_list():
    from app import Products
    try:
        products = Products.query.all()

        products_list = []
        for product in products:
            product_info = {
                'id' : product.id,
                'name' : product.name,
                'price' : product.price
            }
            products_list.append(product_info)

        return jsonify({'products': products_list}), 200
    except ValidationError as e:
        return jsonify(e.messages, 400)
