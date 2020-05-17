import csv
from . import db
from app.api.model.db import db_connection


class Cases:
    """
    Cases model
    """

    def ___init__(self,countryId,countryName,confirmedCases,totalDeaths,totalRecoveries,activeCases,dateOf):
        """
        Initializing the cases variables
        """
        self.countryId = countryId
        self.countryName = countryName
        self.confirmedCases = confirmedCases
        self.totalDeaths = totalDeaths
        self.totalRecoveries = totalRecoveries
        self.activeCases = activeCases
        self.dateOf = dateOf

    def create_case(csvFile):
        """This loads csv file with the latest updates"""
        konnection,kursor = db_connection()
        with open(csvFile,'r') as f:
            next(f)
            kursor.copy_from(f,'cases',sep=',')
        konnection.commit()
        return "Cases updated successfully."
       
    
    def format_cases(iterable):
        """format the data from the database into an iterable list"""
        cases_data = []
        for case_item in iterable:
            case_format = {
                "countryId":case_item[0],
                "countryName":case_item[1],
                "confirmedCases":case_item[2],
                "totalDeaths":case_item[3],
                "totalRecoveries":case_item[4],
                "activeCases":case_item[5],
                "dateOf":case_item[6]
                }
            cases_data.append(case_format)
        return cases_data
    
    def get_last_update_global(dateOf):
        """this gets all global cases last update"""
        get_global = """
        select countryId, countryName,confirmedCases, totalDeaths,totalRecoveries,activeCases
        from cases 
        where dateOf = {} INNER JOIN country on country.countryId = cases.countryId""".format(dateOf)
        return Cases.format_cases(handle_select_queries(get_global))
    
    def get_summary_country(countryName):
        """ this gets the last update for a particular country"""
        get_country_summary = """
        select countryId,countryName,confirmedCases,totalDeaths,totalRecoveries,activeCases
        from cases
        where countryName = {} INNER JOIN country on country.countryId = cases.countryId""".format(countryName)
        return Cases.format_cases(handle_select_queries(get_country_summary))
