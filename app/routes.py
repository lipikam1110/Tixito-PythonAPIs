from flask import Blueprint, request, jsonify
from app.models import User, db
import jwt
from datetime import datetime, timedelta
import secrets
import string
import re

auth_bp = Blueprint('auth', __name__)

# Function to generate a strong secret key
def generate_secret_key(length=32):
    alphabet = string.ascii_letters + string.digits + '-._~'
    secret_key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return secret_key

# Generate a secret key for JWT token signing
SECRET_KEY = generate_secret_key()

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    mobile = data.get('mobile')
    whatsapp_notification_enabled = data.get('whatsappNotificationEnabled', False)

    # Check if email format is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'status': 'failed', 'message': 'Invalid email format'}), 400

    # Check if user already exists by username, email, or mobile number
    user_by_username = User.query.filter_by(username=username).first()
    user_by_email = User.query.filter_by(email=email).first()
    user_by_mobile = User.query.filter_by(mobile=mobile).first()

    if user_by_username:
        return jsonify({'status': 'failed', 'message': 'Username already exists'}), 409

    if user_by_email:
        return jsonify({'status': 'failed', 'message': 'Email already exists'}), 409

    if user_by_mobile:
        return jsonify({'status': 'failed', 'message': 'Mobile number already exists'}), 409

    # Create a new user
    new_user = User(username=username, email=email, mobile=mobile, whatsapp_notification_enabled=whatsapp_notification_enabled)
    db.session.add(new_user)
    db.session.commit()

    # Generate JWT token (for later use)
    jwt_token = generate_jwt_token(new_user)

    # Format response as per the example
    response_data = {
        'status': 'success',
        'data': {
            'token': jwt_token
        }
    }
    return jsonify(response_data), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    mobile = data.get('mobile')

    # Query the database for user with matching email and mobile
    user = User.query.filter_by(email=email, mobile=mobile).first()

    if user:
        # Generate JWT token (for later use)
        jwt_token = generate_jwt_token(user)

        # Format response as per the example
        response_data = {
            'status': 'success',
            'data': {
                'token': jwt_token
            }
        }
        return jsonify(response_data), 200
    else:
        return jsonify({'status': 'failed', 'message': 'Invalid credentials'}), 401

def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(days=1)  # Token expiry time
    }
    # secret_key = current_app.config['SECRET_KEY']
    # jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jwt_token  # Decode bytes to string

