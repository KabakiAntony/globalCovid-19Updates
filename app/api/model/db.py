# this file will handle the db models for this api

import sys
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash
from flask import current_app as app


def db_init():
    """
    Initialize the database
    """
    try:
        konnection, kursor = db_connection()
        db_init_queries =[]
        if app.config['TESTING']:
            print("*** Creating test database tables *** ")
            db_init_queries = drop_tables() + create_tables()
        else:
            print("*** Creating production database tables *** ")
            db_init_queries = create_tables()
        i = 0
        while i != len(db_init_queries):
            query = db_init_queries[i]
            kursor.execute(query)
            konnection.commit()
            i += 1
        createAdmin()
        print("*** Tables are ready ***")
        konnection.close()
    except Exception as error:
        print("We got an error of ->:{} @method db_init".format(error))

def create_tables():
    """
    Create the tables that will hold
    all the data for this simple app
    """
    create_users_table ="""
    CREATE TABLE IF NOT EXISTS users
    (
        userId SERIAL PRIMARY KEY,
        username varchar(25) NOT NULL,
        email VARCHAR (30) NOT NULL UNIQUE,
        password VARCHAR (128) NOT NULL
    )"""

    create_cases_table ="""
    CREATE TABLE IF NOT EXISTS cases
    (
        country varchar(255) NOT NULL,
        confirmedCases INTEGER NOT NULL,
        Deaths INTEGER NOT NULL,
        Recoveries INTEGER NOT NULL,
        activeCases INTEGER NOT NULL,
        dateOf timestamp NOT NULL
    )"""

    return [create_users_table,create_cases_table]

def drop_tables():
    """Drop tables everytime the app restarts"""
    drop_users_table ="""
    DROP TABLE IF EXISTS users CASCADE"""
    drop_cases_table ="""
    DROP TABLE IF EXISTS cases CASCADE"""
    return [drop_users_table,drop_cases_table]


def db_connection(query=None):
    """
    Try connecting to the database if successful
    return the connection and the cursor object
    """
    konnection = None
    kursor = None
    DB_URL = app.config["DATABASE_URI"]
    try:
        konnection = psycopg2.connect(DB_URL)
        kursor = konnection.cursor(cursor_factory=psycopg2.extras.DictCursor)    
        if query:
            kursor.execute(query)
            konnection.commit()

    except (Exception,psycopg2.DatabaseError) as error:
        print("We got an error of ->:{}  @method db_connection".format(error))
    return konnection, kursor

def createAdmin():
    """
    First check if admin was created 
    if not create an admin.dd
    """
    select_user_by_email = """
        SELECT userId, username, password, email FROM users
        WHERE users.email = '{}'""".format("kabaki.antony@gmail.com")

    isAdmin = handle_select_queries(select_user_by_email)
    if not isAdmin:
        konnection,kursor = db_connection()
        password = generate_password_hash('Banuit*123')
        create_admin_if_not_present = """
        INSERT INTO users(username,email, password)
        VALUES('{}', '{}', '{}')""".format('Admin','kabaki.antony@gmail.com', password)
        kursor.execute(create_admin_if_not_present)
        konnection.commit()
        konnection.close()


def handle_other_queries(query,isquery=False):
    """Handles insert/patch/delete queries"""
    konnection,kursor = db_connection(query)
    try:
        if isquery:
            get_last_insert = kursor.fetchone()[0]
            return get_last_insert
        konnection.close()
    except psycopg2.Error as error:
        print("We got an error of ->: {} @method handle_other_queries.".format(error))
        sys.exit(1)

def handle_select_queries(query):
    """Handle select queries"""
    rows = None
    konnection, kursor = db_connection(query)
    try:
        if konnection:
            rows = kursor.fetchall()    
            return rows
        konnection.close()
    except psycopg2.Error as error:
        print("We got an error of ->: {} @method handle_select_queries.".format(error))
