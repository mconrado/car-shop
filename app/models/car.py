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
    __tablename__ = 'cars'
    
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)
    color = db.Column(db.Enum(ColorEnum), nullable=False)
    model = db.Column(db.Enum(ModelEnum), nullable=False)
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"{self.color.value} {self.model.value} (Owner ID: {self.owner_id})"

