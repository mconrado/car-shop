from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Conexão com o MySQL bem-sucedida!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

