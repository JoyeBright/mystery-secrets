from flask import Flask, jsonify, request
from collections import deque
import os

app = Flask(__name__)

# Secrets pool (resets each time server restarts/redeploys)
secrets = deque([
    "Captain Jack Snackrow",
    "Department of Intelligent Systems",
    "R&MD"
])

# Track which IPs already claimed a secret
claimed_ips = {}


def get_client_ip():
    """Return client IP (trust real connection, not spoofable headers)."""
    return request.remote_addr


@app.route("/secret", methods=["GET"])
def get_secret():
    client_ip = get_client_ip()

    # Already claimed → deny
    if client_ip in claimed_ips:
        return jsonify({
            "ip": client_ip,
            "secret": claimed_ips[client_ip],
            "message": "❌ This IP has already claimed a secret"
        }), 403

    # Secrets available → assign one
    if secrets:
        secret = secrets.popleft()
        claimed_ips[client_ip] = secret
        return jsonify({
            "ip": client_ip,
            "secret": secret,
            "message": "✅ New secret assigned"
        }), 200

    # No secrets left → deny
    return jsonify({
        "ip": client_ip,
        "secret": None,
        "message": "❌ No more secrets, expired"
    }), 403


@app.route("/status", methods=["GET"])
def status():
    """Admin/debug: show remaining secrets and claimed IPs count."""
    return jsonify({
        "remaining_secrets": len(secrets),
        "claimed_ips_count": len(claimed_ips)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render will inject $PORT
    app.run(host="0.0.0.0", port=port)
