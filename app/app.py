from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from app.database import db
from app.routes.owner_routes import owner_bp  # Importa o blueprint


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(owner_bp)
@app.route('/')
def index():
    return "API CAR SHOP"

