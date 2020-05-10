import os
import jwt
from flask import jsonify,request,make_response,abort
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
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({"error":"Token is missing"}),401)
        try:
            data = jwt.decode(token,KEY,algorithm="HS256")
            query = """
            SELECT userId,email FROM users
            WHERE users.email = '{}'""".format(data['email'])
            user = handle_select_queries(query)
        except:
            return make_response(jsonify({"error":"Token is expired or invalid"}),401)
        return f(user, *args, **kwargs)
    return decorated