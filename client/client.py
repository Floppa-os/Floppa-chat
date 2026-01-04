import socket
from shared.protocol import create_message, parse_message
from config import HOST, PORT, BUFFER_SIZE

class MessengerClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        self.username = None

    def register(self, username, password):
        msg = create_message('register', {'username': username, 'password': password})
        self.sock.send(msg.encode('utf-8'))
        response = self.sock.recv(BUFFER_SIZE).decode('utf-8')
        return parse_message(response)['data']

    def login(self, username, password):
        msg = create_message('login', {'username': username, 'password': password})
        self.sock.send(msg.encode('utf-8'))
        response = self.sock.recv(BUFFER_SIZE).decode('utf-8')
        success = parse_message(response)['data']
        if success:
            self.username = username
        return success

    def send_message(self, recipient, text):
        msg = create_message('send', {
            'sender': self.username,
            'recipient': recipient,
            'text': text
        })
        self.sock.send(msg.encode('utf-8'))
        response = self.sock.recv(BUFFER_SIZE).decode('utf-8')
        return parse_message(response)['data']

    def get_messages(self):
        msg = create_message('get_messages', {'username': self.username})
        self.sock.send(msg.encode('utf-8'))
        response = self.sock.recv(BUFFER_SIZE).decode('utf-8')
        return parse_message(response)['data']
