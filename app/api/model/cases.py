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
                "asAt":case_item[5]
                }
            cases_data.append(case_format)
        return cases_data
    
    def get_all_countries_latest():
        """this gets all global cases last update"""
        get_global = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where (dateOf::date = current_date and country NOT LIKE 'Global%');"""
        get_global_last = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where  (dateOf::date = current_date -1 and country NOT LIKE 'Global%');
        """
        feeback = Cases.format_cases(handle_select_queries(get_global))
        if not feeback:
            return Cases.format_cases(handle_select_queries(get_global_last))
        return feeback
    
    def get_country_summary(country):
        """ this gets the last update for a particular country"""
        get_summary = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where (country ='{}' or country ='{}') 
        and dateOf::date = current_date ;""".format(country.capitalize(),country)
        get_last_summary = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where (country ='{}' or country ='{}') 
        and dateOf::date = current_date - 1;
        """.format(country.capitalize(),country)
        country_summary_list = Cases.format_cases(handle_select_queries(get_summary))
        if not country_summary_list:
            return Cases.format_cases(handle_select_queries(get_last_summary))
        return country_summary_list
        
    def get_global_summary_latest():
        """get the summary of all countries making a global update"""
        get_global_sum = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where ((dateOf::date = current_date) and country='Global');
        """
        get_global_sum_last = """
        select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where ((dateOf::date = current_date -1) and country='Global');
        """
        global_summary_list = Cases.format_cases(handle_select_queries(get_global_sum))
        if not global_summary_list:
            return Cases.format_cases(handle_select_queries(get_global_sum_last))
        return global_summary_list

    def get_country_historical(country):
        """gets historical data for a particular country since the beginning of this pandemic"""
        get_country_historical_data = """
         select country,confirmedCases,Deaths,Recoveries,activeCases,dateOf
        from cases
        where (country ='{}' or country ='{}');""".format(country.capitalize(),country)
        return Cases.format_cases(handle_select_queries(get_country_historical_data))
    
    def get_country_names():
        """gets the country names"""
        get_country_names_data = """
        select country
        from cases
        where  country NOT like 'Global' 
        AND (dateOf::date = current_date or dateOf::date = current_date-1);"""
        return handle_select_queries(get_country_names_data)
