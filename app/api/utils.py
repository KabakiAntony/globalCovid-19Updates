import os
import re
import jwt
from flask import jsonify,request,make_response,abort,\
    render_template
from functools import wraps
from app.api.model.db import handle_select_queries

KEY = os.getenv('SECRET_KEY')

def token_required(f):
    """
        This function checks to ensure that a token is supplied
        when accessing certain routes.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # if 'x-access-token' in request.headers:
        #     token = request.headers['x-access-token']
        token = request.args.get('in')
        if not token:
            # return override_make_response("error","token is missing",401)
            return render_template('unauthorized.html')
        try:
            data = jwt.decode(token,KEY,algorithm="HS256")
            query = """
            SELECT userId,email FROM users
            WHERE users.email = '{}'""".format(data['email'])
            user = handle_select_queries(query)
        except:
            # return override_make_response("error","token is expired or invalid",401)
            return render_template('invalid-token.html')        
        return f(user, *args, **kwargs)
    return decorated

def isEmail(email):
    """this checks whether an email is valid"""
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        abort(override_make_response("error","email is invalid",400))
    return True


def override_make_response(key,message,status):
    """This method overrides make_response making custom responses from
    views it will be available for various versions of the api hence reducing
    the repetition throughout the code for easy readability"""
    raw_dict = {"status":status}
    raw_dict[key] = message
    return make_response(jsonify(raw_dict),status)

