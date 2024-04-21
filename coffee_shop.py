import sqlite3

def create_database():
    conn = sqlite3.connect('high_end_store.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Product
                 (product_id INTEGER PRIMARY KEY,
                  product_name TEXT NOT NULL,
                  product_price REAL NOT NULL,
                  product_quantity INTEGER NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS Sales
                 (sale_id INTEGER PRIMARY KEY,
                  sale_date TEXT NOT NULL,
                  product_name TEXT NOT NULL,
                  sale_total REAL NOT NULL)''')

    coffees = [('Espresso', 3.0, 100), ('Americano', 2.5, 100), ('Latte', 4.0, 100),
               ('Cappuccino', 4.5, 100), ('Mocha', 4.75, 100), ('Macchiato', 3.5, 100),
               ('Flat White', 3.75, 100), ('Iced Coffee', 3.25, 100),
               ('Cold Brew', 3.5, 100), ('Nitro', 5.0, 100)]
    
    # Clear existing products to prevent duplicates (Optional: Remove this if you want to keep existing data)
    c.execute('DELETE FROM Product')
    
    c.executemany('INSERT INTO Product (product_name, product_price, product_quantity) VALUES (?, ?, ?)', coffees)

    conn.commit()
    conn.close()

class Store:
    def __init__(self):
        self.conn = sqlite3.connect('high_end_store.db')
        self.c = self.conn.cursor()

    def sellProduct(self, product_id, sale_date, sale_quantity):
        self.c.execute('SELECT product_name, product_price, product_quantity FROM Product WHERE product_id = ?', (product_id,))
        product = self.c.fetchone()

        if product:
            if product[2] == 0:
                print("Sorry, this item is sold out. Please choose another.")
            elif product[2] >= sale_quantity:
                new_quantity = product[2] - sale_quantity
                sale_total = product[1] * sale_quantity

                self.c.execute('UPDATE Product SET product_quantity = ? WHERE product_id = ?', (new_quantity, product_id))
                self.c.execute('INSERT INTO Sales (sale_date, product_name, sale_total) VALUES (?, ?, ?)', (sale_date, product[0], sale_total))
                self.conn.commit()
                print(f"Sold {sale_quantity} units of {product[0]}.")
            else:
                print("Sorry the",product,"is sold out, please chose another")
        

    # Include other methods here (addProduct, removeProduct, updateProduct, displayProducts)

    def __del__(self):
        self.conn.close()


create_database()
class Store:
    def __init__(self):
        self.conn = sqlite3.connect('high_end_store.db') # connect to sqlite database
        self.c = self.conn.cursor()

    def addProduct(self, product_name, price, quantity):
        self.c.execute('INSERT INTO Product (product_name, product_price, product_quantity) VALUES (?, ?, ?)', (product_name, price, quantity))
        self.conn.commit()
        print("Product added successfully.") 

    def removeProduct(self, product_id):
        self.c.execute('DELETE FROM Product WHERE product_id = ?', (product_id,))
        self.conn.commit()
        print("Product removed successfully.") 

    def updateProduct(self, product_id, name, price, quantity):
        self.c.execute('UPDATE Product SET product_name = ?, product_price = ?, product_quantity = ? WHERE product_id = ?', (name, price, quantity, product_id))
        self.conn.commit()
        print("Product updated successfully.")

    def displayProducts(self):
        self.c.execute('SELECT * FROM Product')
        for row in self.c.fetchall():
            print(row)

    def sellProduct(self, product_id, sale_date, sale_quantity):
      self.c.execute('SELECT product_name, product_price, product_quantity FROM Product WHERE product_id = ?', (product_id,))
      product = self.c.fetchone()

      if product:
        if product[2] > 0 and product[2] >= sale_quantity:
            # There's enough product to sell
            new_quantity = product[2] - sale_quantity
            sale_total = product[1] * sale_quantity

            self.c.execute('UPDATE Product SET product_quantity = ? WHERE product_id = ?', (new_quantity, product_id))
            self.c.execute('INSERT INTO Sales (sale_date, product_name, sale_total) VALUES (?, ?, ?)', (sale_date, product[0], sale_total))
            self.conn.commit()
            print(f"Sold {sale_quantity} units of {product[0]}.")
        else:
            # Product is found but not enough quantity
            print("Sorry, this item is sold out or not enough quantity available. Please choose another.")
      else:
        # Product doesn't exist
        print("Sorry, we do not have this item available. Hehehe you will not find a bug in my code")

            

    def __del__(self):
        self.conn.close()
def main():
    store = Store()
    while True:
        print("\nWelcome to the High-End Coffee Store Management System")
        print("1. Add a new product")
        print("2. Remove a product")
        print("3. Update a product")
        print("4. Display all products")
        print("5. Sell a product")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            quantity = int(input("Enter the quantity: "))
            store.addProduct(name, price, quantity)
        elif choice == '2':
            product_id = int(input("Enter the product ID to remove: "))
            store.removeProduct(product_id)
        elif choice == '3':
            product_id = int(input("Enter the product ID to update: "))
            name = input("Enter the new product name: ")
            price = float(input("Enter the new product price: "))
            quantity = int(input("Enter the new quantity: "))
            store.updateProduct(product_id, name, price, quantity)
        elif choice == '4':
            store.displayProducts()
        elif choice == '5':
            product_id = int(input("Enter the product ID to sell: "))
            sale_date = input("Enter the sale date (YYYY-MM-DD): ")
            sale_quantity = int(input("Enter the quantity sold: "))
            store.sellProduct(product_id, sale_date, sale_quantity)
        elif choice == '6':
            print("Thank you for shopping with High-End Coffee. Goodbye! Enjoy the ENergy")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main() 
