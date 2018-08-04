from flask import Flask

app = Flask(__name__)


@app.route('/add/a=<a>&b=<b>')
def add(a, b):
    return str(float(a) + float(b))


@app.route('/sub/a=<a>&b=<b>')
def add(a, b):
    return str(float(a) - float(b))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
