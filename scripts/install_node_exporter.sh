#!/usr/bin/env bash

# Install the node exporter and enable
wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz -O node_exporter.tar.gz

tar -xvf node_exporter.tar.gz

sudo mv node_exporter*/node_exporter /usr/local/bin

sudo useradd -rs /bin/false node_exporter

sudo touch /etc/systemd/system/node_exporter.service

sudo echo -en "[Unit]\nDescription=Node Exporter\nAfter=network.target\n\n[Service]\nUser=node_exporter\nGroup=node_exporter\nType=simple\nExecStart=/usr/local/bin/node_exporter\n\n[Install]\nWantedBy=multi-user.target\n" | sudo tee /etc/systemd/system/node_exporter.service


# Enable and run
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter
sudo systemctl status node_exporter

sudo ufw allow 9100

echo "Add $(hostname -I | awk '{print $1}'):9100 to your node_exporter file"


rm -rfv node_exporter*
