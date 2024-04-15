from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from api.models import User, db
from flask_mail import Message
from api.utils import mail
from flask_cors import CORS
from . import user_bp

CORS(user_bp)


@user_bp.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).first()

    if user is None:
            return jsonify({"msg": "Bad Request"}), 404

    if email == user.email and password == user.password:
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200
    
    else: 
            return jsonify({"msg": "Bad email or password. I am sorry"}), 401


@user_bp.route("/valid-token", methods=["GET"])
@jwt_required()
def valid_token():
     
     current_user = get_jwt_identity()

     querty_results = User.query.filter_by(email=current_user).first()

     if querty_results is None:
            return jsonify({"msg": "user does not exist",
                           "is_logged": False}), 404
     
     return jsonify({"is_logged": True}), 200

#post endpoint to retrieve the user email, check if it is real, and send recovery link
@user_bp.route("/recover-password", methods=["POST"])
def recover_password():
    email = request.json.get("email", None)
    frontend_url = request.json.get("frontend_url", None)

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"msg": "Bad Request"}), 404

    # Generate a token for the user
    access_token = create_access_token(identity=email)

    # Create a password recovery link
    password_recovery_link = f"{frontend_url}/{access_token}"

    # Send the password recovery email
    msg = Message(
        "Password Recovery",
        recipients=[email],
        html=f"<p>Please click the following link to reset your password:</p><a href='{password_recovery_link}'>Reset Password</a>"
    )
    mail.send(msg)
    return jsonify({"msg": "Password recovery email sent"}), 200




@user_bp.route('/create-user', methods=['POST'])
def create_user():
      data = request.json
      user_exists = User.query.filter_by(email=data["email"]).first()
      if user_exists is None: 
            new_user = User(
                  email= data['email'],
                  password= data['password'],
                  is_active= data['is_active']
                )
            db.session.add(new_user)
            db.session.commit()
            return jsonify({
                  "msg": "new user successfully created"
            }), 200
      else: 
            return jsonify({
                  "msg": "this email is already used by a user"
            }), 400

@user_bp.route('/reset-password', methods=['PUT'])
@jwt_required()
def reset_password():
    current_user = get_jwt_identity()
    data = request.json
    user = User.query.filter_by(email=current_user).first()
    if user is None: 
        return jsonify({"msg": "user does not exist",
                            "is_logged": False}), 404
    else: 
        user.password = data["password"]
        db.session.commit()
        return ({"msg": "ok, the password has been updated in the database"}), 200
