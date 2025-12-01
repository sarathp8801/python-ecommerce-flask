import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Indian@123",
        database="ecommerce_db"
    )
    return connection
