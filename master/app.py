from flask import Flask, request, jsonify
import threading
import random

app = Flask(__name__)

# Dictionary to store active games
games = {}

@app.route('/health', methods=['GET'])
def health():
    return 'healthy', 200

@app.route('/start_game', methods=['POST'])
def start_game():
    game_id = str(random.randint(1, 100000))
    min_number = int(request.json['min_number'])
    max_number = int(request.json['max_number'])
    target_number = random.randint(min_number, max_number)

    games[game_id] = {
        'min_number': min_number,
        'max_number': max_number,
        'target_number': target_number,
        'history': [],
    }

    return jsonify({"message": "Game started", "game_id": game_id}), 200

@app.route('/play_game/<game_id>', methods=['GET'])
def play_game(game_id):
    if game_id not in games:
        return jsonify({"message": "Game not found"}), 404

    game = games[game_id]

    guess = random.randint(game['min_number'], game['max_number'])
    game['history'].append(guess)

    if guess < game['target_number']:
        response = {"message": "higher", "history": game['history']}
    elif guess > game['target_number']:
        response = {"message": "lower", "history": game['history']}
    else:
        response = {"message": "won", "history": game['history']}

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
