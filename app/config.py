import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config:
    DB_USER = os.getenv('DB_USER') 
    DB_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('MYSQL_DATABASE')

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

