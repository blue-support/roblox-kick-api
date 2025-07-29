from flask import Flask, request, jsonify
app = Flask(__name__)

kicklist = set()  # Set für Namen der Spieler, die aktuell gekickt werden sollen

@app.route('/kick', methods=['POST'])
def kick_player():
    data = request.json
    username = data.get('username')
    reason = data.get('reason', 'Du wurdest gekickt!')

    if not username:
        return jsonify({'error': 'Kein Spielername angegeben'}), 400

    # Füge Spieler zur Kicklist hinzu
    kicklist.add(username)

    # Hier würdest du den Kick an Roblox senden (z.B. über HTTP Request an dein Roblox Spiel)
    # Zum Beispiel: roblox_kick(username, reason)  <-- Implementiere diese Funktion

    return jsonify({'message': f'{username} wird gekickt'}), 200

@app.route('/kicklist', methods=['GET'])
def get_kicklist():
    return jsonify(list(kicklist))

@app.route('/removekick', methods=['POST'])
def remove_kick():
    data = request.json
    username = data.get('username')

    if username in kicklist:
        kicklist.remove(username)
        return jsonify({'message': f'{username} aus Kicklist entfernt'}), 200
    return jsonify({'error': 'Spieler nicht in Kicklist'}), 404

if __name__ == '__main__':
    app.run()

