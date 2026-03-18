import json

def load_devices():
    with open('devices.json') as f:
        return json.load(f)["devices"]

def authenticate(device_id, key):
    devices = load_devices()
    for d in devices:
        if d["id"] == device_id and d["key"] == key:
            return True
    return False
