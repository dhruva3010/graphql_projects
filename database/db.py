import mysql.connector

def get_db_connection():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Myaccount321$",
        database="db_test"
    )
    return db_connection
