from flask import request, jsonify
from src.models.models import db, User

# Route to create user
def create_user():
    try:
        datos = request.json
        new_user = User(
            identification=datos['identification'],
            name=datos['name'],
            email=datos['email'],
            password=datos['password'],
            type=datos['type']
        )
        new_user.set_password(datos['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400