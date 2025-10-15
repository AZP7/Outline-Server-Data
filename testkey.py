#!/usr/bin/env python3
import json, base64

# Load your Shadowsocks config
config = {
    "server": "0.0.0.0",
    "port_password": {
        "8381": "foobar1",
        "8382": "foobar2",
        "8383": "foobar3",
        "8384": "foobar4",
        "8385": "foobar5",
        "8386": "foobar6",
        "8387": "foobar7",
        "8389": "foobar9",
        "8390": "foobar10",
        "8391": "foobar11",
        "8392": "foobar12",
        "8393": "foobar13",
        "8394": "foobar14",
        "8395": "foobar15",
        "8396": "foobar16",
        "8397": "foobar17",
        "8398": "foobar18",
        "8399": "foobar19",
        "8400": "foobar20"
    },
    "timeout": 300,
    "method": "chacha20-ietf-poly1305"
}

# 🔧 Replace with your actual server IP or domain
SERVER = "ns.quickaccessmm.shop"   # e.g. "167.172.76.216"
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
