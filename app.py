import os
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(BASE_DIR, "log.txt")

def log_ip_to_file(ip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] IP: {ip}\n"
    
    with open(LOG_FILE_PATH, "a") as f:
        f.write(log_entry)
    print(f"--- Logged {ip} to {LOG_FILE_PATH} ---", flush=True)

@app.route('/')
def get_ip():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.remote_addr
    
    log_ip_to_file(ip)
    return f"Your IP Address is: {ip} (Logged)"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)