import os
import jwt
import psycopg2
from flask import request,abort,render_template
from app.api import globalUpdatesBlueprint
from app.api.model.users import Users
from app.api.utils import isEmail,token_required,override_make_response

KEY = os.getenv('SECRET_KEY','9hqhBvIEfq5qEWyHklFxMIJES_c')

@globalUpdatesBlueprint.route('/auth/admin', methods=['GET'])
def show_login_UI():
    """
    Return admin login interface
    """
    return render_template('login.html')


@globalUpdatesBlueprint.route('/auth/admin/signin', methods=['POST'])
def authenticate_admin():
    """Authenticate user details"""
    try:
        data = request.get_json()
        email = data["email"]
        enteredPassword = data["password"]
    except KeyError:
        abort(override_make_response("error","Keys should be email,password",400))
    isEmail(email)
    try:
        user = Users.get_user_by_email(email)
        if not user:            
            abort(override_make_response("error","User does not exist please check email",404))
        # format the returned user
        userId = user[0][0]
        email = user[0][1]
        returned_password = user[0][2]
        password_check = Users.compare_password(returned_password,enteredPassword)

        if not password_check:
            abort(override_make_response("error","The password is wrong, please try again",401))

        token = jwt.encode({"email" :email},KEY,algorithm="HS256")

        return override_make_response("data",token.decode('utf-8'),200)
    except psycopg2.DatabaseError as _error:
        abort(make_response(jsonify({"Error":"Server error"}),500))



@globalUpdatesBlueprint.route('/auth/admin/upload')
@token_required
def uploads(user):
    """
    Return upload ui
    """
    return render_template('upload.html')
    

    

        
    