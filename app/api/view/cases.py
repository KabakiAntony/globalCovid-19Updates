import os
import csv
import jwt
import psycopg2
from flask import request,abort,jsonify
from werkzeug.utils import secure_filename
from app.api import globalUpdatesBlueprint
from app.api.utils import token_required,override_make_response
from app.api.model.cases import Cases
from app.api.model.db import db_connection

#uploadFolder = os.getenv('UPLOAD_FOLDER')

@globalUpdatesBlueprint.route('/auth/admin/upload/cases',methods=['POST'])
@token_required
def upload_cases(user):
    """Here the admin updates the cases table"""
    email = user[0][1]
    if str(email) == "kabaki.antony@gmail.com":
        try:  
            konnection,kursor = db_connection()
            receivedFile = request.files['caseCsv']
            secureFilename = secure_filename(receivedFile.filename)
            receivedFile.save(os.path.join(secureFilename))
            feedback = Cases.create_case(secureFilename)
            return override_make_response("data",feedback,200)

        except (Exception,psycopg2.DatabaseError) as err:
            return override_make_response("error","Database error of : {} ".format(err),400)

    return override_make_response("error","Only the admin can load data into the db",401)

@globalUpdatesBlueprint.route('/country/<countryName>',methods=['GET'])
def get_country_data(countryName):
    """Get only a particular country's data"""
    feedback = Cases.get_country_summary(countryName)
    if not feedback:
        return override_make_response("error","No data found",404)
    return override_make_response("data",feedback,200)

@globalUpdatesBlueprint.route('/historical/country/<countryName>',methods=['GET'])
def get_country_historical_data(countryName):
    """Get only a particular country's data from the beginning"""
    feedback = Cases.get_country_historical(countryName)
    if not feedback:
        return override_make_response("error","No data found",404)
    return override_make_response("data",feedback,200)

@globalUpdatesBlueprint.route('/global/summary',methods=['GET'])
def get_latest_global():
    """Get the latest for the whole globe"""
    feedback = Cases.get_global_summary_latest()
    feedbackI = Cases.get_all_countries_latest()
    global_country_list = feedback + feedbackI
    return override_make_response("data",global_country_list,200)


@globalUpdatesBlueprint.route('/global',methods=['GET'])
def get_latest_global_sum():
    """Get the latest for the whole globe"""
    feedback = Cases.get_global_summary_latest()
    return override_make_response("data",feedback,200)

       