from flask import Flask, request, jsonify

app = Flask(__name__)

kick_list = []

@app.route('/kick', methods=['POST'])
def kick_player():
    data = request.get_json()
    username = data.get("username")
    reason = data.get("reason", "Kein Grund angegeben")

    if not username:
        return jsonify({"error": "Kein Benutzername angegeben"}), 400

    # Prüfen, ob Spieler schon auf der Liste ist - wenn ja, Grund updaten
    for entry in kick_list:
        if entry['username'].lower() == username.lower():
            entry['reason'] = reason
            break
    else:
        # Spieler zur Kickliste hinzufügen
        kick_list.append({"username": username, "reason": reason})

    return jsonify({"message": f"{username} wurde zur Kickliste hinzugefügt."}), 200


@app.route('/checkkick/<username>', methods=['GET'])
def check_kick(username):
    global kick_list
    # Suche Spieler in der Liste
    for entry in kick_list:
        if entry['username'].lower() == username.lower():
            reason = entry["reason"]
            # Spieler aus der Liste entfernen, damit nur einmal gekickt wird
            kick_list = [k for k in kick_list if k['username'].lower() != username.lower()]
            return jsonify({"kick": True, "reason": reason})

    return jsonify({"kick": False})


@app.route('/kicklist', methods=['GET'])
def get_kicklist():
    return jsonify(kick_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
