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
        "8388": "foobar8",
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
        "8400": "foobar20",
        "8401": "foobar21",
        "8402": "foobar22",
        "8403": "foobar23",
        "8404": "foobar24",
        "8405": "foobar25",
        "8406": "foobar26",
        "8407": "foobar27",
        "8408": "foobar28",
        "8409": "foobar29",
        "8410": "foobar30",
        "8411": "foobar31",
        "8412": "foobar32",
        "8413": "foobar33",
        "8414": "foobar34",
        "8415": "foobar35",
        "8416": "foobar36",
        "8417": "foobar37",
        "8418": "foobar38",
        "8419": "foobar39",
        "8420": "foobar40",
        "8421": "foobar41",
        "8422": "foobar42",
        "8423": "foobar43",
        "8424": "foobar44",
        "8425": "foobar45",
        "8426": "foobar46",
        "8427": "foobar47",
        "8428": "foobar48",
        "8429": "foobar49",
        "8430": "foobar50",
    },
    "timeout": 300,
    "method": "chacha20-ietf-poly1305"
}
# 🔧 Replace with your actual server IP or domain
SERVER = "ss.quickaccessmm.shop"   # e.g. "167.172.76.216"
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

# Save as JSON file
with open("/home/welcome/E/Project/Python/Outline-Server-Data/outline_keys.json", "w") as f:
    json.dump(keys, f, indent=4)

print("✅ outline_keys.json created successfully!")


# [Unit]
# Description=Shadowsocks Server
# After=network.target

# [Service]
# ExecStart=/usr/bin/env bash -c 'sudo /snap/bin/shadowsocks.ssserver -c /var/snap/shadowsocks/common/shadowsocks.json'
# Restart=always
# User=root
# WorkingDirectory=/root

# [Install]
# WantedBy=multi-user.target

# [Unit]
# Description=Shadowsocks Server
# After=network.target

# [Service]
# ExecStart=/snap/bin/shadowsocks.ssserver -c /var/snap/shadowsocks/comm>
# Restart=always
# User=root
# WorkingDirectory=/root

# [Install]
# WantedBy=multi-user.target