from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/add/a=<a>&b=<b>')
    def add(a, b):
        return str(float(a) + float(b))

    @app.route('/sub/a=<a>&b=<b>')
    def sub(a, b):
        return str(float(a) - float(b))

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app


if __name__ == '__main__':
    create_app().run()
