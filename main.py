from flask import Flask, request, jsonify

app = Flask(__name__)

kick_list = []

@app.route('/kick', methods=['POST'])
def add_kick():
    data = request.json
    username = data.get('username')
    reason = data.get('reason', 'Kein Grund angegeben')

    if not username:
        return jsonify({"error": "Kein Benutzername angegeben"}), 400

    for entry in kick_list:
        if entry['username'] == username:
            return jsonify({"message": "Spieler ist bereits gekickt"}), 200

    kick_list.append({"username": username, "reason": reason})
    return jsonify({"message": f"{username} wurde zur Kickliste hinzugefügt"}), 200

@app.route('/kicklist', methods=['GET'])
def get_kicklist():
    return jsonify({"kicks": kick_list})

@app.route('/clearkicks', methods=['POST'])
def clear_kicks():
    kick_list.clear()
    return jsonify({"message": "Kickliste geleert"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
