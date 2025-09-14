from flask import Flask, jsonify, request

app = Flask(__name__)

# Secrets pool
secrets = ["Captain Jack Snackrow", "Department of Intelligent Systems", "R&MD"]

# Track claimed IPs
claimed_ips = {}

@app.route("/secret")
def get_secret():
    # Get real client IP (considering proxies)
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    # If IP already has a secret
    if client_ip in claimed_ips:
        return jsonify({
            "secret": f"❌ IP {client_ip} has already claimed: {claimed_ips[client_ip]}"
        }), 403

    # If secrets are left
    if secrets:
        secret = secrets.pop(0)
        claimed_ips[client_ip] = secret
        return jsonify({"ip": client_ip, "secret": secret})

    # No more secrets
    return jsonify({"secret": "❌ No more secrets, expired."}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
