from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")


@socketio.on("connect")
def on_connect():
    print(f"user connect sid {request.sid}")

@socketio.on("JOIN")
def on_join(data):
    username = data["username"]
    room = data["room"]
    join_room(room)
    emit("USER_JOINED",f"{username} has entered the room", room=room)

@socketio.on("SEND_MESSAGE") 
def on_send_message(message):
    print(message)
    emit("RELAY_MESSAGE", message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
