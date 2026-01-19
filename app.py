import os
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

log_path = "/app/logs/log.txt"

def log_ip_to_file(ip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] IP: {ip}\n"
    
    with open(log_path, "a") as f:
        f.write(log_entry)
    print(f"--- Logged {ip} to {log_path} ---", flush=True)

@app.route('/')
def get_ip():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.remote_addr
    
    log_ip_to_file(ip)
    return f"Your IP Address is: {ip} (Logged)"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

    #asdgsdzsa