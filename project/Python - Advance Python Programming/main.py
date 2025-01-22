import tkinter as tk
from tkinter import messagebox
from product_manager import ProductManager
from customer import Customer

class ProductManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management")
        self.root.geometry("500x500")

        self.product_manager = None
        self.customer = None

        self.create_widgets()

    def create_widgets(self):
        self.login_label = tk.Label(self.root, text="Login", font=("Arial", 16))
        self.login_label.pack(pady=10)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "adminpassword":
            self.product_manager = ProductManager(username, password)
            self.show_product_manager_interface()
        elif username == "customer" and password == "customerpassword":
            self.customer = Customer(username, password)
            self.show_customer_interface()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def show_product_manager_interface(self):
        self.clear_screen()
        self.manager_label = tk.Label(self.root, text="Product Manager Interface", font=("Arial", 16))
        self.manager_label.pack(pady=10)

        self.add_product_button = tk.Button(self.root, text="Add Product", command=self.add_product)
        self.add_product_button.pack(pady=10)

        self.view_stocks_button = tk.Button(self.root, text="View All Products", command=self.view_all_products)
        self.view_stocks_button.pack(pady=10)

    def add_product(self):
        self.clear_screen()
        self.add_product_label = tk.Label(self.root, text="Add New Product", font=("Arial", 16))
        self.add_product_label.pack(pady=10)

        self.product_name_label = tk.Label(self.root, text="Product Name:")
        self.product_name_label.pack()
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.pack()

        self.price_label = tk.Label(self.root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack()

        self.stock_label = tk.Label(self.root, text="Stock Quantity:")
        self.stock_label.pack()
        self.stock_entry = tk.Entry(self.root)
        self.stock_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_product)
        self.submit_button.pack(pady=20)

    def submit_product(self):
        product_name = self.product_name_entry.get()
        price = float(self.price_entry.get())
        stock_quantity = int(self.stock_entry.get())

        if product_name and price > 0 and stock_quantity > 0:
            self.product_manager.manage_product_stock(product_name, price, stock_quantity)
            messagebox.showinfo("Product Added", "Product added successfully!")
        else:
            messagebox.showerror("Invalid Data", "Please enter valid data.")

    def view_all_products(self):
        products = self.product_manager.view_all_stocks()
        self.clear_screen()

        self.view_products_label = tk.Label(self.root, text="All Products", font=("Arial", 16))
        self.view_products_label.pack(pady=10)

        for product in products:
            product_text = f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}"
            product_label = tk.Label(self.root, text=product_text)
            product_label.pack()

        self.back_button = tk.Button(self.root, text="Back", command=self.show_product_manager_interface)
        self.back_button.pack(pady=20)

    def show_customer_interface(self):
        self.clear_screen()
        self.customer_label = tk.Label(self.root, text="Customer Interface", font=("Arial", 16))
        self.customer_label.pack(pady=10)

        self.purchase_button = tk.Button(self.root, text="Purchase Product", command=self.purchase_product)
        self.purchase_button.pack(pady=10)

    def purchase_product(self):
        self.clear_screen()

        self.product_id_label = tk.Label(self.root, text="Product ID:")
        self.product_id_label.pack()
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.pack()

        self.quantity_label = tk.Label(self.root, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_purchase)
        self.submit_button.pack(pady=20)

    def submit_purchase(self):
        product_id = int(self.product_id_entry.get())
        quantity = int(self.quantity_entry.get())

        if self.customer:
            success, message = self.customer.purchase_product(product_id, quantity)
            messagebox.showinfo("Purchase Status", message)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductManagementApp(root)
    root.mainloop()





