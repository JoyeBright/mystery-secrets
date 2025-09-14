from flask import Flask, jsonify, request
from collections import deque
import os

app = Flask(__name__)

# Ephemeral in-memory secrets pool (resets on every deploy)
secrets = deque([
    "Captain Jack Snackrow",
    "Department of Intelligent Systems",
    "R&MD"
])

# Track claimed IPs in memory (resets every deploy)
claimed_ips = {}


def get_client_ip():
    """Return the actual client IP (Render proxies pass it correctly)."""
    return request.headers.get("X-Forwarded-For", request.remote_addr)


@app.route("/secret", methods=["GET"])
def get_secret():
    client_ip = get_client_ip()

    # Already claimed?
    if client_ip in claimed_ips:
        return jsonify({
            "ip": client_ip,
            "secret": claimed_ips[client_ip],
            "message": "❌ This IP has already claimed a secret"
        }), 403

    # Still secrets available?
    if secrets:
        secret = secrets.popleft()
        claimed_ips[client_ip] = secret
        return jsonify({
            "ip": client_ip,
            "secret": secret,
            "message": "✅ One secret only per IP"
        }), 200

    # No more secrets
    return jsonify({
        "ip": client_ip,
        "secret": None,
        "message": "❌ No more secrets, expired"
    }), 403


@app.route("/status", methods=["GET"])
def status():
    """Admin endpoint: check remaining secrets & claims."""
    return jsonify({
        "remaining_secrets": len(secrets),
        "claimed_ips": len(claimed_ips)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
