from argparse import ArgumentParser
from flask import Flask, jsonify, request
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer

app = Flask(__name__, instance_relative_config=True)

@app.route('/invoke', methods=['POST'])
def get_invoke():
    m = request.args.get('m')
    f = request.args.get('f')

    scope = request.get_json(force=True)

    scope = {
        'm': m,
        'f': f,
        'args': [],
        'kwargs': {},
        **scope
    }

    result = eval(f'getattr(__import__(m), f)(*args, **kwargs)', scope)
    return jsonify(result)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--address", 
                        default="127.0.0.1", 
                        type=str, 
                        help="Address IP or URL. Default value is 127.0.0.1")

    parser.add_argument("--port", 
                        default=9000, 
                        type=int, 
                        help="Port to listen. Default value is 9000")

    args = parser.parse_args()
    
    application = HTTPServer(WSGIContainer(app))
    application.listen(args.port, address=args.address)
    IOLoop.instance().start()