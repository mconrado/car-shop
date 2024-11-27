from app import db


class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    sales_o = db.Column(db.Boolean, nullable=False, default=True)
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return self.name
