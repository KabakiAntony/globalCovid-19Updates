from . import db

class Cases:
    """
    Cases model
    """

    def ___init__(self,countryId,confirmedCases,totalDeaths,totalRecoveries,activeCases,dateOf):
        """
        Initializing the cases variables
        """
        self.countryId = countryId
        self.confirmedCases = confirmedCases
        self.totalDeaths = totalDeaths
        self.totalRecoveries = totalRecoveries
        self.activeCases = activeCases
        self.dateOf = dateOf

    def create_case(self):
        """This posts latest cases updates"""
        insert_latest_cases ="""
        insert into cases(countryId,confirmedCases,totalDeaths, totalrecoveries,activeCases,dateOf)
        values('{}','{}','{}','{}','{}','{}') returning caseId;
        """.format(self.countryId,self.confirmedCases,self.totalDeaths,self.totalRecoveries,self.activeCases,self.dateOf)
        return db.handle_other_queries(insert_latest_cases)
    
    def format_cases(iterable):
        """format the data from the database into an iterable list"""
        cases_data = []
        for case_item in iterable:
            case_format = {
                "caseId":case_item[0],
                "countryId":case_item[1],
                "countryName":case_item[2],
                "confirmedCases":case_item[3],
                "totalDeaths":case_item[4],
                "totalRecoveries":case_item[5],
                "activeCases":case_item[6]
                }
            cases_data.append(case_format)
        return cases_data
    
    def get_last_update_global(dateOf):
        """this gets all global cases last update"""
        get_global = """
        select caseId, countryId, countryName,confirmedCases, totalDeaths,totalRecoveries,activeCases
        from cases 
        where dateOf = {} inner join country on country.countryId = cases.countryId
        """.format(dateOf)
        return Cases.format_cases(handle_select_queries(get_global))
    
    def get_summary_country(countryName):
        """ this gets the last update for a particular country"""
        get_country_summary = """
        select countryId,countryName,confirmedCases,totalDeaths,totalRecoveries,activeCases
        from cases
        where countryName = {}  inner join country on country.countryId = cases.countryId
        """.format(countryName)
        return Cases.format_cases(handle_select_queries(get_country_summary))
