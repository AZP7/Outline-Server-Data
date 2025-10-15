ShadowSocks Guide 
--------------------
1.apt-get install python-pip

2.enable python .venv
  
  .sudo apt install python3-venv
  .python3 -m venv .venv 
  .source .venv/bin/activate
  .install the pip package" pip install git+https://github.com/shadowsocks/shadowsocks.git@master
 "
3.Create a file at the "/etc/systemd/system/shadowsocks.service"

4.add the code to the previous files "step3"

 "
[Unit]
Description=Shadowsocks Server
After=network.target

[Service]
ExecStart=/usr/bin/env bash -c 'sudo /snap/bin/shadowsocks.ssserver -c /var/snap/shadowsocks/common/shadowsocks.json'
Restart=always
User=root
WorkingDirectory=/root

[Install]
WantedBy=multi-user.target
"
5.modified the config file

nano /var/snap/shadowsocks/common/shadowsocks.json

paste your config file

6.restart the server 

 .systemctl daemon-reload
 .systemctl restart shadowsocks
 .systemctl status shadowsocks

7.Install the  "vnstat" command to check the databandwidth for the server

.sudo apt update
.sudo apt install vnstat -y
.sudo systemctl enable vnstat
.sudo systemctl start vnstat
.vnstat
.vnstat -d   # daily
.vnstat -w   # weekly
.vnstat -m   # monthly