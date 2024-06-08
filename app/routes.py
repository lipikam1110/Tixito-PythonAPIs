from flask import Blueprint, request, jsonify
from app.models import User, db
import bcrypt  # Import bcrypt library

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    mobile = data.get('mobile')

    # Check if user already exists by username or mobile number
    user_by_username = User.query.filter_by(username=username).first()
    user_by_mobile = User.query.filter_by(mobile=mobile).first()

    if user_by_username:
        return jsonify({'Status': 'Failed', 'Message': 'Username already exists'}), 409

    if user_by_mobile:
        return jsonify({'Status': 'Failed', 'Message': 'Mobile number already exists'}), 409

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(username=username, password=hashed_password.decode('utf-8'), mobile=mobile)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'Message':'User Created Succussfully','Status': 'Success','Data':{'Token':f'{hashed_password}'}}), 201
    # return jsonify({'Message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    mobile = data.get('mobile')
    password = data.get('password')

    user = User.query.filter_by(mobile=mobile).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'Message': 'Login successfully','Status': 'Success','Data':{'Token':f'{user.password.encode('utf-8')}'}}), 200
    else:
        return jsonify({'Message': 'Invalid credentials','Status': 'Failed'}), 401
