import jwt
import psycopg2
from flask import request,abort
from werkzeug.utils import secure_filename
from app.api import globalUpdatesBlueprint
from app.api.utils import token_required,override_make_response
from app.api.model.country import Country

@globalUpdatesBlueprint.route('/auth/admin/upload/country',methods=['POST'])
@token_required
def upload_cases(user):
    """Here the admin updates the countries table"""
    email = user[0][1]
    if str(email) == "kabaki.antony@gmail.com":
        try:  
            receivedFile = request.files['countryCsv']
            secureFilename = secure_filename(receivedFile.filename)
            receivedFile.save(os.path.join(secureFilename))
            feedback = Country.upload_countries(secureFilename)
            return override_make_response("data",feedback,200)

        except (Exception,psycopg2.DatabaseError) as error:
            return override_make_response("error","we got this error of  {} loading the file ".format(error),200)

    return override_make_response("error","Only the admin can load data into the db",401)
