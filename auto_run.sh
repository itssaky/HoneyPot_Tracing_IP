#!/bin/bash

sudo apt update && sudo apt upgrade -y

# Install Python and required libraries
sudo apt install -y python3 python3-pip
pip3 install --upgrade smtplib

sudo ufw allow 8080/tcp

mkdir -p ~/honeypot
cd ~/honeypot

# Run the honeypot in the background
nohup python3 honeypot.py > honeypot.log 2>&1 &


echo "Honeypot setup complete and running on port 8080!"