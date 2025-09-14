from flask import Flask, jsonify

app = Flask(__name__)

# 3 top secrets, handed out one by one
secrets = ["Captain Jack Snackrow", "Department of intelligent system", "R&MD"]

@app.route("/secret")
def get_secret():
    if secrets:
        return jsonify({"secret": secrets.pop(0)})
    else:
        return jsonify({"secret": "❌ No more secrets, expired."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
