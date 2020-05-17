import csv
from . import db
from app.api.model.db import db_connection


class Country:
    """
    country model
    """

    def __init__(self,countryId,countryName):
        """Initialize attribs of a country"""
        self.countryId = countryId
        self.countryName = countryName
    
    def upload_countries(countryCsv):
        """Save country data into the db"""
        konnection,kursor = db_connection()
        with open(countryCsv,'r') as f:
            next(f)
            kursor.copy_from(f,'country',sep=',')
        konnection.commit()
        return "Country info uploaded successfully"
