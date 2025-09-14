from flask import Flask, jsonify, request
from collections import deque
import os

app = Flask(__name__)

# Secrets pool
secrets = deque([
    "Captain Jack Snackrow",
    "Department of Intelligent Systems",
    "R&MD"
])

# Track claimed IPs
claimed_ips = {}


@app.route("/secret")
def get_secret():
    # Use actual connection IP (not spoofable headers)
    client_ip = request.remote_addr

    if client_ip in claimed_ips:
        return jsonify({
            "ip": client_ip,
            "secret": claimed_ips[client_ip],
            "message": "❌ Already claimed"
        }), 403

    if secrets:
        secret = secrets.popleft()
        claimed_ips[client_ip] = secret
        return jsonify({
            "ip": client_ip,
            "secret": secret,
            "message": "✅ One secret only per student"
        }), 200

    return jsonify({
        "ip": client_ip,
        "secret": None,
        "message": "❌ No more secrets, expired"
    }), 403


if __name__ == "__main__":
    # Render sets the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
