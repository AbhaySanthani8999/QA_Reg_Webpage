from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for Streamlit interaction

@app.route('/register', methods=['POST'])
def register():
    data = request.json

    # Basic validations
    required_fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'gender', 'dob', 'country', 'terms']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'success': False, 'message': f'Missing field: {field}'}), 400

    if data['password'] != data['confirm_password']:
        return jsonify({'success': False, 'message': 'Passwords do not match'}), 400

    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return jsonify({'success': False, 'message': 'Invalid email format'}), 400

    # Simulate user creation
    response = {
        'success': True,
        'message': 'User registered successfully!',
        'data': {
            'full_name': f"{data['first_name']} {data['last_name']}",
            'email': data['email'],
            'gender': data['gender'],
            'dob': data['dob'],
            'country': data['country']
        }
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
