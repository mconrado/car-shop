from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config, TestConfig
from app.database import db
from app.routes.owner_routes import owner_bp
from app.routes.car_routes import car_bp
import os

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'testing':
    app.config.from_object(TestConfig)
else:
    app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(owner_bp)
app.register_blueprint(car_bp)
@app.route('/')
def index():
    return "API CAR SHOP"
