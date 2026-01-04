import socket
import threading
from shared.protocol import parse_message, create_message
import database
from config import HOST, PORT, BUFFER_SIZE

def handle_client(conn, addr):
    print(f"Клиент подключился: {addr}")
    while True:
        try:
            data = conn.recv(BUFFER_SIZE).decode('utf-8')
            if not data:
                break
            msg = parse_message(data)
            if not msg:
                continue

            action = msg['action']
            data = msg['data']

            if action == 'register':
                success = database.register_user(data['username'], data['password'])
                response = create_message('register_result', success)
            elif action == 'login':
                success = database.authenticate(data['username'], data['password'])
                response = create_message('login_result', success)
            elif action == 'send':
                success = database.send_message(data['sender'], data['recipient'], data['text'])
                response = create_message('send_result', success)
            elif action == 'get_messages':
                msgs = database.get_messages(data['username'])
                response = create_message('messages', msgs)
            else:
                response = create_message('error', 'Неизвестное действие')

            conn.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Ошибка с клиентом {addr}: {e}")
            break
    conn.close()
    print(f"Клиент отключился: {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Сервер запущен на {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
