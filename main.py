from flask import Flask, request, jsonify

app = Flask(__name__)

kick_list = []  # speichert: [{"username": "...", "reason": "..."}]

@app.route("/kick", methods=["POST"])
def kick():
    data = request.json
    username = data.get("username")
    reason = data.get("reason", "Du wurdest gekickt!")
    
    # Überschreibe vorhandenen Kick für den Spieler (damit immer nur 1 Eintrag)
    global kick_list
    kick_list = [k for k in kick_list if k["username"] != username]
    
    # Füge neuen Kick-Eintrag hinzu
    kick_list.append({"username": username, "reason": reason})
    return jsonify({"status": "ok"})

@app.route("/kicklist", methods=["GET"])
def get_kicklist():
    return jsonify({"kicks": kick_list})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)



