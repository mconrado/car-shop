from flask import Flask



app = Flask(__name__)

@app.route('/')
def index():
    return "Conexão com o MySQL bem-sucedida!sdaf"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

