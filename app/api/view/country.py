import os
import csv
#import jwt
import psycopg2
from flask import request,abort,jsonify
from werkzeug.utils import secure_filename
from app.api import globalUpdatesBlueprint
from app.api.utils import token_required,override_make_response
from app.api.model.country import Country
from app.api.model.db import db_connection

@globalUpdatesBlueprint.route('/auth/admin/upload/country',methods=['POST'])
@token_required
def upload_country(user):
    """Here the admin updates the countries table"""
    email = user[0][1]
    if str(email) == "kabaki.antony@gmail.com":
        try: 
            konnection,kursor = db_connection() 
            receivedFile = request.files['countryCsv']
            secureFilename = secure_filename(receivedFile.filename)
            receivedFile.save(os.path.join(secureFilename))
            feedback = Country.upload_countries(secureFilename)
            # with open(secureFilename,'r') as f:
            #     next(f)
            #     kursor.copy_from(f,'country',sep=',')
            #     konnection.commit()
            return override_make_response("data",feedback,200)

        except (Exception,psycopg2.DatabaseError) as err:
            return override_make_response("error","Database error occured  {} ".format(err),400)

    return override_make_response("error","Only the admin can load data into the db",401)
