To run this honeypot on your Raspberry Pi, follow these steps:

# 1. Prepare Your Raspberry Pi
```
Make sure your Raspberry Pi is connected to the network.
Update your system packages:
    sudo apt update && sudo apt upgrade -y
```

# 2. Install Python and Required Libraries
```
Your Raspberry Pi should already have Python3 installed. If not, install it:

    sudo apt install python3 python3-pip -y
Install the required Python libraries:

    pip3 install --upgrade smtplib
```
# 3. Edit the Script with Your Email Credentials
```
Open the script:

    nano honeypot.py
Change the SMTP settings:
Replace smtp.example.com with your email provider’s SMTP server (e.g., smtp.gmail.com for Gmail).
Use your email and password (or an app password if using Gmail).
```
# 4. Allow the Script to Use the Port (If Needed)
```
If running on a lower port (below 1024), allow Python to bind to it:

    sudo setcap 'cap_net_bind_service=+ep' $(which python3)
If using a firewall, allow the port:

    sudo ufw allow 8080/tcp
```
# 5. Run the Honeypot

```
Start the script:
    python3 honeypot.py
It will now listen for unauthorized connections and log attempts.
```
# 6. Run in Background (Optional)
```
To keep it running after logout:
    nohup python3 honeypot.py > honeypot.log 2>&1 &
```
# 7. View Logs
```
Check connection attempts:
    cat honeypot_log.txt
```
# 8. Using Auto RUn
```
    chmod +x setup_honeypot.sh
Run the script:
    ./setup_honeypot.sh
```