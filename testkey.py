#!/usr/bin/env python3
import json, base64

# Load your Shadowsocks config
config = {
    "server": "0.0.0.0",
    "port_password": {
        "8414": "foobar34",
        "8415": "foobar35",
        "8416": "foobar36",
    },
    "timeout": 300,
    "method": "chacha20-ietf-poly1305"
}


# 🔧 Replace with your actual server IP or domaind
SERVER = "inn.quickaccessmm.shop"   # e.g. "167.172.76.216"
METHOD = config["method"]

def make_key(method, password, host, port):
    userinfo = f"{method}:{password}".encode()
    b64 = base64.urlsafe_b64encode(userinfo).decode().rstrip("=")
    return f"ss://{b64}@{host}:{port}"

# Build dictionary of port → key
keys = {
    port: make_key(METHOD, pwd, SERVER, port)
    for port, pwd in config["port_password"].items()
}

print(keys)
# Save as JSON file
# with open("/home/welcome/E/Project/Python/Outline-Server-Data/outline_keys.json", "w") as f:
#     json.dump(keys, f, indent=4)

# print("✅ outline_keys.json created successfully!")
