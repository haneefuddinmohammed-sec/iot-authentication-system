failed_attempts = {}

def detect_threat(device_id):
    if device_id not in failed_attempts:
        failed_attempts[device_id] = 0

    failed_attempts[device_id] += 1

    if failed_attempts[device_id] >= 3:
        print(f"[ALERT] Suspicious activity from {device_id}")
