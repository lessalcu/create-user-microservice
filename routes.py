from flask import request, jsonify
from models import db, Usuario

# Route to create user
def create_user():
    try:
        datos = request.json
        nuevo_usuario = Usuario(
            nombre=datos['name'],
            email=datos['email'],
            contrasena=datos['password']
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'mistake': str(e)}), 400