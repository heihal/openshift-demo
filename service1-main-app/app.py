from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-message', methods=['GET'])
def get_message():
    try:
        response = requests.get('http://service2-message-app:5000/message')
        message = response.json().get('message', 'No message received')
    except Exception as e:
        message = f'Error fetching message: {str(e)}'
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)