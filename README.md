# Floppa-chat
Мессенджер:
messenger/
├── server/
│   ├── __init__.py
│   ├── main.py
│   └── database.py
├── client/
│   ├── __init__.py
│   ├── ui.py
│   └── client.py
├── shared/
│   ├── __init__.py
│   └── protocol.py
├── config.py
└── requirements.txt
# Данные сервера
Для хоста используется переменная host.
Для порта используется переменная port.
# Переменные по умолчанию
HOST = '127.0.0.1'
PORT = 8888
BUFFER_SIZE = 1024HOST = '127.0.0.1'
PORT = 8888
BUFFER_SIZE = 1024
## конфиг с переменными хоста
main.py
