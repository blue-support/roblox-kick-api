from flask import Flask, request, jsonify

app = Flask(__name__)

kicklist = set()  # Spieler, die gekickt werden sollen

@app.route('/kick', methods=['POST'])
def kick():
    data = request.json
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Kein Spielername angegeben'}), 400

    kicklist.add(username)
    return jsonify({'message': f'{username} wurde zur Kickliste hinzugefügt'}), 200

@app.route('/kicklist', methods=['GET'])
def get_kicklist():
    # Einfach Liste zurückgeben
    return jsonify(list(kicklist)), 200

@app.route('/confirmkick', methods=['POST'])
def confirm_kick():
    data = request.json
    username = data.get('username')
    if username in kicklist:
        kicklist.remove(username)
        return jsonify({'message': f'{username} aus Kickliste entfernt'}), 200
    return jsonify({'error': 'Spieler nicht in Kickliste'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)




