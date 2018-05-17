import json
from uuid import uuid4
from flask import Flask, request


def process_query_string(qs):
    params = request.query_string.decode().split('&')
    keys = {}

    for p in params:
        pair = p.split('=')
        keys[pair[0]] = pair[1]

    return keys


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        message = '''
        Routes:<br/><br/>

        '/': Show this page<br/>
        '/hello': Says hello<br/>
        '/hello?name=<your name>': Says hello to you!<br/>
        '/secret': Tells you a secret
        '''

        return message, 200

    @app.route('/hello', methods=['GET'])
    def hello():
        message = "Hello!"
        qs = request.query_string

        if len(qs) > 0:
            name = process_query_string(qs).get('name', 'Human')
            message = 'Hello {}!'.format(name)

        return message, 200

    @app.route('/secret')
    def secret():
        secret = "This is a secret: {}<br/><br/>Don't tell anyone."
        return secret.format(uuid4().hex), 200

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
