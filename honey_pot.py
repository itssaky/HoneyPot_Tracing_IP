import socket
import datetime
import smtplib
from email.mime.text import MIMEText

# Configuration
HOST = "0.0.0.0"  
PORT = 0 # Linsting all the ports        
LOG_FILE = "honeypot_log.txt"
ADMIN_EMAIL = "akyraj113@gmail.com"  
SMTP_SERVER = "smtp.gmail.com "  
SMTP_PORT = 587
SMTP_USERNAME = "honeypot@gmail.com"  
SMTP_PASSWORD = "honey_pass_password"  

def send_alert(ip, port):
    
    subject = "Honeypot Alert: Unauthorized Access Attempt"
    body = f"An unauthorized access attempt was detected from {ip}:{port} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USERNAME
    msg['To'] = ADMIN_EMAIL
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, ADMIN_EMAIL, msg.as_string())
        print("Alert email sent to admin.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

def log_attempt(ip, port):
    """Log connection attempts."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Connection attempt from {ip}:{port}\n"
    print(log_entry, end="")
    with open(LOG_FILE, "a") as log:
        log.write(log_entry)
    send_alert(ip, port)

def start_honeypot():
    """Start the honeypot server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Honeypot running on {HOST}:{PORT}...")
        
        while True:
            conn, addr = server_socket.accept()
            log_attempt(addr[0], addr[1])
            conn.sendall(b"Unauthorized access attempt detected.\n")
            conn.close()

if __name__ == "__main__":
    start_honeypot()
