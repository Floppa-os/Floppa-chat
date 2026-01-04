users = {}  # {username: password}
messages = {}  # {recipient: [(sender, text), ...]}

def register_user(username, password):
    if username in users:
        return False
    users[username] = password
    messages[username] = []
    return True

def authenticate(username, password):
    return users.get(username) == password

def send_message(sender, recipient, text):
    if recipient in messages:
        messages[recipient].append((sender, text))
        return True
    return False

def get_messages(username):
    return messages.get(username, [])
