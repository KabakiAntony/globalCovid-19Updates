import csv
from . import db
from app.api.model.db import db_connection,handle_select_queries


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
                "country":case_item[0],
                "confirmedCases":case_item[1],
                "Deaths":case_item[2],
                "Recoveries":case_item[3],
                "activeCases":case_item[4],
                "dateOf":case_item[5]
                }
            cases_data.append(case_format)
        return cases_data
    
    def get_all_countries_latest():
        """this gets all global cases last update"""
        get_global = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where dateOf = current_date;"""
        return Cases.format_cases(handle_select_queries(get_global))
    
    def get_country_summary(country):
        """ this gets the last update for a particular country"""
        get_summary = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where (country ='{}' or country ='{}') and dateOf = current_date;
        """.format(country.capitalize(),country)
        return Cases.format_cases(handle_select_queries(get_summary))
    
    def get_global_summary_latest():
        """get the summary of all countries making a global update"""
        get_global_sum = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where (dateOf = current_date and country='Global');
        """
        return Cases.format_cases(handle_select_queries(get_global_sum))

    def get_country_historical(country):
        """gets historical data for a particular country since the beginning of this pandemic"""
        get_country_historical_data = """
         select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where (country ='{}' or country ='{}');""".format(country.capitalize(),country)
        return Cases.format_cases(handle_select_queries(get_country_historical_data))
