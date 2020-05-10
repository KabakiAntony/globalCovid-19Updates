import os
import jwt
import psycopg2
from flask import request,abort,jsonify
from app.api import globalUpdatesBlueprint
from app.api.utils import token_required
from app.api.model.cases import Cases

@globalUpdatesBlueprint.route('/global',methods=['POST'])
# @token_required
def upload_cases():
    """Here the admin updates the cases table"""
    # try:
    #     email = user[0][1]
    #     if email == "kabaki.antony@gmail.com":
    # except:
    #     return make_response(jsonify({"Error":"Only the admin that can post updates"}),401)
    try:
        case_load_data = request.get_json()
        print(case_load_data)  
        # content = post_data["content"]
        # new_post = Lists(content=content,user_id=user_id)
        # post_id = new_post.create_post_item()
        # return override_make_response("Data",[{"content":content,"post_id":post_id}],201)
    except psycopg2.DatabaseError as error:
        return make_response(jsonify({"error":"an error occured"}),400)