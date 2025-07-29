from flask import Flask, request, jsonify

app = Flask(__name__)

pending_kicks = {}

@app.route("/kick", methods=["POST"])
def kick():
    data = request.get_json()
    username = data.get("username")
    reason = data.get("reason", "Kein Grund angegeben")
    if username:
        pending_kicks[username.lower()] = reason
        return jsonify({"success": True, "message": f"{username} wird gekickt."})
    return jsonify({"success": False, "message": "Kein Username angegeben."}), 400

@app.route("/get_kick/<username>", methods=["GET"])
def get_kick(username):
    reason = pending_kicks.pop(username.lower(), None)
    if reason:
        return jsonify({"kick": True, "reason": reason})
    return jsonify({"kick": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
