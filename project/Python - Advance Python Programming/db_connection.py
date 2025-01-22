import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    
    try:
       
        connection = sqlite3.connect(db_file)
        print("SQLite connection established.")
        return connection
    except Error as e:
        print(f"Error while connecting to SQLite: {e}")
        return None


