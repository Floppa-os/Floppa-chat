import json

def create_message(action, data=None):
    return json.dumps({'action': action, 'data': data})

def parse_message(raw):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None
