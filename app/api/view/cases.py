import os
import csv
import jwt
import psycopg2
from flask import request,abort,jsonify
from werkzeug.utils import secure_filename
from app.api import globalUpdatesBlueprint
from app.api.utils import token_required,override_make_response
from app.api.model.cases import Cases


uploadFolder = os.getenv('UPLOAD_FOLDER')

@globalUpdatesBlueprint.route('/auth/admin/upload/cases',methods=['POST'])
@token_required
def upload_cases(user):
    """Here the admin updates the cases table"""
    email = user[0][1]
    if str(email) == "kabaki.antony@gmail.com":
        try:  
            receivedFile = request.files['csvFile']
            secureFilename = secure_filename(receivedFile.filename)
            receivedFile.save(os.path.join(secureFilename))
            print(secureFilename)
            feedback = Cases.create_case(secureFilename)
            return override_make_response("data",feedback,200)
        except (Exception,psycopg2.DatabaseError) as error:
            return override_make_response("error","we got this error of  {} loading the file ".format(error),200)

    return override_make_response("error","Only the admin can load data into the db",401)
       