# tests for user go here
import unittest
import json
from app import create_app
from app.api.model.db import db_init,createAdmin


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up tests"""
        
        self.app = create_app("testing")
        self.client = self.app.test_client()
        db_init()
        self.no_password_field = {"email":"kabaki.kiarie@gmail.com"}
        self.non_existent_user = {"email":"akabaki.kiarie@gmail.com","password":"Baniut*123"}
        self.no_email_field = {"password":"Banuit*123"}
        self.correct_user = {"email":"kabaki.antony@gmail.com","password":"Banuit*123"}
        self.wrong_password = {"email":"kabaki.antony@gmail.com","password":"Banuitw123"}
        

    def tearDown(self):
        """Clear the db after tests finish running"""
        db_init()

    def test_successful_user_login(self):
        """Test login """
        createAdmin()
        response = self.client.post(
            "/auth/admin/signin", 
            data=json.dumps(self.correct_user)
            ,content_type="application/json")
        self.assertEqual(response.status_code, 200)

    
    def test_signin_with_wrong_password(self):
        """Test sign in with a wrong password"""
        createAdmin()
        response = self.client.post(
            "/auth/admin/signin", 
            data=json.dumps(self.wrong_password)
            ,content_type="application/json")
        self.assertEqual(response.status_code, 401)

    def test_signin_non_existent_user(self):
        createAdmin()
        """Test sign in a non-existent user"""
        response = self.client.post(
            "/auth/admin/signin", 
            data=json.dumps(self.non_existent_user)
            ,content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_signin_an_email_key_missing(self):
        """Test signing with the email field missing"""
        response = self.client.post(
            "/auth/admin/signin", 
            data=json.dumps(self.no_email_field)
            ,content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_signin_password_key_missing(self):
        """Test signing with the password field missing"""
        response = self.client.post(
            "/auth/admin/signin", 
            data=json.dumps(self.no_password_field)
            ,content_type="application/json")
        self.assertEqual(response.status_code, 400)





    

