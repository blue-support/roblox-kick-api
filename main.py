from flask import Flask, request, jsonify

app = Flask(__name__)
pending_kicks = {}

@app.route("/kick", methods=["POST"])
def kick_player():
    data = request.get_json()
    username = data.get("username")
    reason = data.get("reason", "Kein Grund angegeben")
    if username:
        pending_kicks[username.lower()] = reason
        return jsonify({"status": "ok"}), 200
    return jsonify({"error": "Username fehlt"}), 400

@app.route("/get_kick/<username>", methods=["GET"])
def get_kick(username):
    reason = pending_kicks.pop(username.lower(), None)
    if reason:
        return jsonify({"kick": True, "reason": reason})
    return jsonify({"kick": False}), 200

@app.route("/")
def home():
    return "Kick API läuft", 200
