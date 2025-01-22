import sqlite3
from db_connection import create_connection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        
        conn = create_connection("product_db.sqlite")
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                           (self.username, self.password))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "User registered successfully!"
        return False, "Registration failed"

    def login(self):
        
        conn = create_connection("product_db.sqlite")
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                           (self.username, self.password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user:
                return True, "Login successful!"
            else:
                return False, "Invalid username or password"
        return False, "Connection failed"

