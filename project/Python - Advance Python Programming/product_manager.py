from db_connection import create_connection
from user import User

class ProductManager(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def manage_product_stock(self, product_name, price, stock_quantity):
        
        conn = create_connection("product_db.sqlite") 
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, stock_quantity) VALUES (?, ?, ?)", 
                       (product_name, price, stock_quantity))
        conn.commit()
        cursor.close()
        conn.close()

    def view_all_stocks(self):
       
        conn = create_connection("product_db.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


