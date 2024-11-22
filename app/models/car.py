from app import db
import enum


class ColorEnum(enum.Enum):
    YELLOW = "yellow"
    BLUE = "blue"
    GRAY = "gray"


class ModelEnum(enum.Enum):
    HATCH = "hatch"
    SEDAN = "sedan"
    CONVERTIBLE = "convertible"


class Car(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"), nullable=False)
    color = db.Column(db.Enum(ColorEnum), nullable=False)
    model = db.Column(db.Enum(ModelEnum), nullable=False)
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"{self.color.value} {self.model.value} (Owner ID: {self.owner_id})"

    @staticmethod
    def can_add_car(owner_id):
        car_count = Car.query.filter_by(owner_id=owner_id).count()
        return car_count < 3

    @classmethod
    def create_car(cls, owner_id, color, model):
        new_car = cls(owner_id=owner_id, color=color, model=model)
        db.session.add(new_car)
        db.session.commit()
        return new_car

    def __init__(self, owner_id, color, model):
        if not self.can_add_car(owner_id):
            raise Exception("Um proprietário não pode ter mais de 3 carros.")
        self.owner_id = owner_id
        self.color = color
        self.model = model
