from db_connection import create_connection
from user import User

class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.__balance = 0  

    def register(self):
        
        conn = create_connection("product_db.sqlite")
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customers (username, password, balance) VALUES (?, ?, ?)", 
                           (self.username, self.password, self.__balance))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Customer registered successfully!"
        return False, "Registration failed"

    def login(self):
        conn = create_connection("product_db.sqlite")
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE username = ? AND password = ?", 
                           (self.username, self.password))
            customer = cursor.fetchone()
            cursor.close()
            conn.close()
            if customer:
                return True, "Login successful!"
            else:
                return False, "Invalid username or password"
        return False, "Connection failed"

    def purchase_product(self, product_id, quantity):
        conn = create_connection("product_db.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT price, stock_quantity FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        if product and product[1] >= quantity:
            total_price = product[0] * quantity
            self.__balance -= total_price  
            cursor.execute("UPDATE products SET stock_quantity = stock_quantity - ? WHERE id = ?", 
                           (quantity, product_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True, f"Purchased successfully for {total_price}!"
        cursor.close()
        conn.close()
        return False, "Product not available or insufficient stock"


