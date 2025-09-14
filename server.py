from flask import Flask, jsonify, request
from collections import deque

app = Flask(__name__)

secrets = deque([
    "Captain Jack Snackrow",
    "Department of Intelligent Systems",
    "R&MD"
])

claimed_ips = {}

@app.route("/secret")
def get_secret():
    # Trust only the actual connection IP
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
