from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.database import db 

app = Flask(__name__)
app.config.from_object('app.config.Config')
db.init_app(app)

