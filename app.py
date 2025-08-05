from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from Streamlit

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    required_fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'gender', 'dob', 'country', 'terms']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'success': False, 'message': f'Missing field: {field}'}), 400

    if data['password'] != data['confirm_password']:
        return jsonify({'success': False, 'message': 'Passwords do not match'}), 400

    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return jsonify({'success': False, 'message': 'Invalid email format'}), 400

    return jsonify({
        'success': True,
        'message': 'User registered successfully!',
        'data': {
            'full_name': f"{data['first_name']} {data['last_name']}",
            'email': data['email'],
            'gender': data['gender'],
            'dob': data['dob'],
            'country': data['country']
        }
    }), 200

if __name__ == '__main__':
    # This version avoids issues with signal handling
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
