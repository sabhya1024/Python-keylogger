import platform
import socket

def get_system_info():
    system_info = {
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        # "hostname": socket.gethostname(),
    }
    return system_info
