from flask import Blueprint, request, jsonify
from app.models.car import Car
from app import db

car_bp = Blueprint("car", __name__)


@car_bp.route("/car", methods=["POST"])
def create_car():
    try:
        data = request.get_json()

        if "owner_id" not in data or "color" not in data or "model" not in data:
            return jsonify({"message": "Owner ID, cor e modelo são obrigatórios."}), 400

        new_car = Car(
            owner_id=data["owner_id"], color=data["color"], model=data["model"]
        )
        db.session.add(new_car)
        db.session.commit()

        return jsonify(
            {
                "message": "Carro criado com sucesso.",
                "id": new_car.id,
                "owner_id": new_car.owner_id,
                "color": new_car.color.value,
                "model": new_car.model.value,
                "creation_date": new_car.creation_date,
            }
        ), 201

    except Exception as e:
        return jsonify({"message": "Erro ao criar carro.", "error": str(e)}), 500


@car_bp.route("/car/<int:car_id>", methods=["GET"])
def get_car(car_id):
    try:
        car = db.session.get(Car, car_id)

        if car is None:
            return jsonify({"message": "Carro não encontrado."}), 404

        return jsonify(
            {
                "id": car.id,
                "owner_id": car.owner_id,
                "color": car.color.value,
                "model": car.model.value,
                "creation_date": car.creation_date,
            }
        ), 200

    except Exception as e:
        return jsonify({"message": "Erro ao buscar carro.", "error": str(e)}), 500
