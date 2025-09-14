from flask import Flask, jsonify, request

app = Flask(__name__)

# 3 top secrets, handed out one by one
secrets = ["Captain Jack Snackrow", "Department of Intelligent Systems", "R&MD"]

# Track which IPs already claimed a secret
claimed_ips = {}

@app.route("/secret")
def get_secret():
    client_ip = request.remote_addr

    # If this IP has already claimed a secret
    if client_ip in claimed_ips:
        return jsonify({
            "secret": f"❌ IP {client_ip} has already claimed: {claimed_ips[client_ip]}"
        }), 403

    # If there are still secrets available
    if secrets:
        secret = secrets.pop(0)
        claimed_ips[client_ip] = secret
        return jsonify({
            "ip": client_ip,
            "secret": secret
        })
    else:
        return jsonify({"secret": "❌ No more secrets, expired."}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
