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
    return "I expect to recieve a csv file"
    # try:
    #     email = user[0][1]
    #     if email == "kabaki.antony@gmail.com":
    # except:
    #     return make_response(jsonify({"Error":"Only the admin that can post updates"}),401)
    # try:
    #     case_load_data = request.get_json()
    #     countryId = case_load_data["countryId"]
    #     confirmedCases = case_load_data["confirmedCases"]
    #     totalDeaths = case_load_data["totalDeaths"]
    #     totalRecoveries = case_load_data["totalRecoveries"]
    #     activeCases = case_load_data["activeCases"]
    #     deathOf = case_load_data["deathOf"]
    #     new_case_update = Cases(\
    #         countryId = countryId,confirmedCases = confirmedCases,\
    #         totalDeaths = totalDeaths,totalRecoveries = totalRecoveries,\
    #         activeCases = activeCases,dateOf = dateOf)
    #     caseId = new_case_update.create_case()
    #     return make_response(jsonify({}),201)
    # except psycopg2.DatabaseError as error:
        