from flask import Blueprint, jsonify, request
from models import db, Person, Planet, User, Favorite  

api_bp = Blueprint('api', __name__)

# Rutas para Personas
@api_bp.route('/people', methods=['GET'])
def get_people():
    people = Person.query.all()
    return jsonify([{'id': p.id, 'name': p.name} for p in people])

@api_bp.route('/people', methods=['POST'])
def add_person():
    data = request.json
    new_person = Person(name=data['name'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'id': new_person.id, 'name': new_person.name}), 201

@api_bp.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = Person.query.get_or_404(people_id)
    return jsonify({'id': person.id, 'name': person.name})

# Rutas para Planetas
@api_bp.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([{'id': p.id, 'name': p.name} for p in planets])

@api_bp.route('/planets', methods=['POST'])
def add_planet():
    data = request.json
    new_planet = Planet(name=data['name'])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({'id': new_planet.id, 'name': new_planet.name}), 201

@api_bp.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    return jsonify({'id': planet.id, 'name': planet.name})

# Rutas para Usuarios
@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username} for u in users])

@api_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

# Rutas para Favoritos
@api_bp.route('/favorite/user/<int:favorite_user_id>', methods=['POST'])
def add_favorite_user(favorite_user_id):
    user_id = request.args.get('user_id')
    favorite = Favorite(user_id=user_id, favorite_user_id=favorite_user_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({'message': 'Favorite user added'}), 201

@api_bp.route('/favorite/user/<int:favorite_user_id>', methods=['DELETE'])
def delete_favorite_user(favorite_user_id):
    user_id = request.args.get('user_id')
    favorite = Favorite.query.filter_by(user_id=user_id, favorite_user_id=favorite_user_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite user deleted'}), 204
    return jsonify({'message': 'Favorite not found'}), 404

@api_bp.route('/users/favorites', methods=['GET'])
def get_favorites():
    user_id = request.args.get('user_id')
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    return jsonify([{'favorite_user_id': f.favorite_user_id} for f in favorites])
