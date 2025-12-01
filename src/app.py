from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a и b - НЕ числа'
    return str(a * b)

if __name__ == '__main__':
    app.run(debug=True, port=8080)