from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def get_message():
    return jsonify(message="Hello from demo-service 2!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)