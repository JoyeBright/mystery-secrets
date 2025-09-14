from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Reset secrets fresh at every server start
secrets = ["Captain Jack Snackrow", "Department of Intelligent Systems", "R&MD"]

# File to track claimed IPs
CLAIMED_FILE = "claimed_ips.txt"

# Always start with a clean file and empty dict
claimed_ips = {}
open(CLAIMED_FILE, "w").close()

@app.route("/secret")
def get_secret():
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    # If this IP has already claimed a secret
    if client_ip in claimed_ips:
        return jsonify({
            "secret": f"❌ IP {client_ip} has already claimed: {claimed_ips[client_ip]}"
        }), 403

    # If there are still secrets available
    if secrets:
        secret = secrets.pop(0)
        claimed_ips[client_ip] = secret

        # Save claim to file
        with open(CLAIMED_FILE, "a") as f:
            f.write(f"{client_ip}={secret}\n")

        return jsonify({
            "ip": client_ip,
            "secret": secret
        })
    else:
        return jsonify({"secret": "❌ No more secrets, expired."}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
