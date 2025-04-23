from flask import Blueprint, request, jsonify, session
from flask_mail import Mail, Message
from datetime import datetime
from .utils import generate_and_store_otp, otp_storage
from flask_login import login_user, login_required, logout_user
from .user import User

auth_bp = Blueprint('auth', __name__)

mail = Mail()

@auth_bp.record_once
def setup(state):
    mail.init_app(state.app)


@auth_bp.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    email = data.get('email')

    print(f"📨 Received OTP request for: {email}")

    try:
        otp = generate_and_store_otp(email)

        msg = Message("Your OTP Code", recipients=[email])
        msg.body = f"Your OTP is {otp}"

        print("📤 Attempting to send email...")

        mail.send(msg)

        print("✅ Email sent successfully!")
        return jsonify({"message": "OTP sent successfully"}), 200

    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return jsonify({"error": "Failed to send OTP"}), 500


@auth_bp.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data.get('email')
    otp = data.get('otp')

    if not email or not otp:
        return jsonify({'error': 'Email and OTP are required'}), 400
    
    record = otp_storage.get(email)

    if not record:
        return jsonify({'error': 'No OTP found for this email'}), 404
    
    if datetime.now() > record['expires']:
        return jsonify({'error': 'OTP has expired'}), 401
    
    if otp == record['otp']:
        user = DBUser.query.filter_by(email=email).first()
        if not user:
            user = DBUser(email=email, role='citizen')
            db.session.add(user)
            db.session.commit()
            
        login_user(user)
        print("✅ User logged in:", user.email)

        return jsonify({'message': 'OTP verified successfully ✅'}), 200   
                 
    return jsonify({'error': 'Invalid OTP'}), 403
    

@auth_bp.route('/mock-login', methods=["POST"])
def mock_login():
    data = request.get_json()
    email = data.get('email')
    role = data.get('role')

    session['email'] = email
    session['user_role'] = role

    return jsonify({'message': f'Logged in as {role}'}), 200


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user() 
    return jsonify({'message': 'Logged out successfully ✅'}), 200
