# import unittest
# import json
# import os
# import jwt
# from io import BytesIO
# from app import create_app
# from app.api.model.db import db_init

# KEY = os.getenv('SECRET_KEY')

# class TestCases(unittest.TestCase):

#     def setUp(self):
#         """Set up tests"""
        
#         self.app = create_app("testing")
#         self.client = self.app.test_client() 
#         db_init()       

#     def tearDown(self):
#         """Clear the db after tests finish running"""
#         db_init()

#     def post(self, data={}):
#         """this posts data for routes that need data"""
#         #'file': (BytesIO(b'FILE CONTENT'), 'globalCovid19Updates-5-19-2020.csv')
#         file = os.path.join('globalCovid19Updates-5-19-2020.csv')
#         data = {"file":file}
#         #token = jwt.encode({"email":"kabaki.antony@gmail.com"},KEY,algorithm='HS256') ?in={token} content_type='multipart/form-data',
#         # ,data=data
#         response = self.client.post('/auth/admin/upload/cases')
#         return response

    
#     def test_updating_cases(self):
#         """test updating cases"""
#         response = self.post()
#         self.assertEqual(response.status_code,200)
    
#     def test_getting_a_country_data(self):
#         """test getting latest country update"""
#         resp = self.post()
#         self.assertEqual(resp.status_code,200)
#         response = self.client.get('/country/{}'
#         .format('Kenya'))
#         self.assertEqual(response.status_code,200)


#     def test_getting_a_country_historical_data(self):
#         """test getting a country historical data"""
#         resp = self.post()
#         self.assertEqual(resp.status_code,200)
#         response = self.client.get('/historical/country/{}'
#         .format('Kenya'))
#         self.assertEqual(response.status_code,200)

    
#     def test_getting_a_global_data(self):
#         """test getting latest number for the globe"""
#         # resp = self.post()
#         # self.assertEqual(resp.status_code,200)
#         response = self.client.get('/global')
#         self.assertEqual(response.status_code,200)

#     def test_getting_a_global_summary(self):
#         """test getting latest numbers for the globe & countries"""
#         resp = self.post()
#         self.assertEqual(resp.status_code,200)
#         response = self.client.get('/global/summary')
#         self.assertEqual(response.status_code,200)
