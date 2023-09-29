from flask import Flask, request, jsonify
import random

app = Flask(__name__)
min_number = 1
max_number = 1000
target_number = random.randint(min_number, max_number)
history = []

@app.route('/health', methods=['GET'])
def health():
    return 'healthy', 200

@app.route('/hostname', methods=['GET'])
def hostname():
    return request.host, 200

@app.route('/play', methods=['GET'])
def play():
    global target_number
    global history

    guess = random.randint(min_number, max_number)
    history.append(guess)

    if guess < target_number:
        response = {"message": "higher", "history": history}
    elif guess > target_number:
        response = {"message": "lower", "history": history}
    else:
        response = {"message": "won", "history": history}

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
