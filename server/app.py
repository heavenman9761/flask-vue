from logging import DEBUG
from os import name
from flask import Flask, jsonify, request
from flask.helpers import make_response, url_for
from flask_cors import CORS
from flask_restx import Api, Resource
from flask_restx import namespace
from flask_restx.namespace import ResourceRoute
from route.books import Books
from route.users import Users
from route.builditgw import BuildIt
from route.maechul import MaeChul
from models.database import db_session
from models.Model import TbUsers
from flask import Flask, render_template, session 
from flask_socketio import SocketIO, emit
import json
import requests
from gevent import monkey

# from socketio.server import SocketIOServer

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={
    r'/*':{'origins':'*'}
    # r'/books/*':{'origins':'*'},
    # r'/users/*':{'origins':'*'},
    # r'/buildit-gw/*':{'origins':'*'}
})

socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')
# monkey.patch_all()

api = Api(app)
api.add_namespace(Books, '/books')
api.add_namespace(Users, '/users')
api.add_namespace(BuildIt, '/buildit-gw')
api.add_namespace(MaeChul, '/maechul')

socket_clients = []

def show_tables(): 
    queries = db_session.query(TbUsers) 
    entries = [dict(userid=q.userid, name=q.name, password=q.password) for q in queries] 
    print(entries)

@api.route('/aaa')
class toNaver(Resource):
    def get(self):
        params = {
            "param1": "test1",
            "param2": 123,
            "param3": "한글"
        }
        res = requests.post('http://127.0.0.1:5001/receiver', data=json.dumps(params))

@api.route('/ping')
class ping_pong(Resource):
    def get(self):
        show_tables()
        return jsonify('pong!')

@api.route('/iotdata')
class iotdata(Resource):
    def post(self):
        post_data = json.loads(request.get_data(), encoding='utf-8')
        socketio.start_background_task(target=lambda: server_push(post_data))
        # socketio.sleep(1)

def server_push(data):
    with app.app_context():
        socketio.emit('respose', data, namespace='/myroom')
        # socketio.sleep(1)

@socketio.on('connect', namespace='/myroom')
def connect():
    print("====================connect")
    emit("respose", {'msg': 'Welcome SocketIO World'})

@socketio.on('disconnect', namespace='/myroom') 
def disconnect(): 
    session.clear() 
    print("====================Disconnected")
    
# @socketio.on("request", namespace='/myroom') 
# def request(message): 
#     emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
    socketio.run(app)

    # SocketIOServer(('0.0.0.0', 5000), app, resource='socket.io').serve_forever()
