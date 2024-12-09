def get_customers():
    workouts = Workouts.query.all()
    return workouts_schema.jsonify(workouts)

def get_customer(customer_id):
    pass

def add_customer():
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
 
def update_customer(customer_id):
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

def delete_customer(customer_id):
    pass
    # workout = Members.query.get_or_404(member_id, workout_id)
    # db.session.delete(workout)
    # db.session.commit()
    # return jsonify({'message': 'Workout removed'}), 200

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