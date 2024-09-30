from flask import Blueprint, request, jsonify
from app.models.owner import Owner
from app.validators import is_valid_email
from app import db

owner_bp = Blueprint('owner', __name__)

@owner_bp.route('/owner', methods=['POST'])
def create_owner():
    try:
        data = request.get_json()
        
        if 'name' not in data or 'email' not in data:
            return jsonify({"message": "Nome e email são obrigatórios."}), 400
        
        if not is_valid_email(data['email']):
            return jsonify({"message": "Email inválido."}), 400
        
        new_owner = Owner(name=data['name'], email=data['email'])
        db.session.add(new_owner)
        db.session.commit()
        
        return jsonify({"message": "Proprietário criado com sucesso.", "id": new_owner.id, "name": new_owner.name, "email": new_owner.email}), 201

    except Exception as e:
        return jsonify({"message": "Erro ao criar proprietário.", "error": str(e)}), 500
