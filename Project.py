import sqlite3
from datetime import datetime
from abc import ABC, abstractmethod

# Person Manager Class
class PersonManager:
    @abstractmethod
    def insert_person(self):
        pass

    @abstractmethod
    def remove_person(self):
        pass

    @abstractmethod
    def display_all(self):
        pass

# Employee Manager Class
class EmployeeManager(PersonManager):
    def insert_person(self):
        name = input("\nEnter employee name: ")
        surname = input("Enter employee surname: ")
        cell = input("Enter employee cell: ")
        email = input("Enter employee email: ")

        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("INSERT INTO Employees (Name, Surname, `Cell Number`, Email) VALUES (?, ?, ?, ?)", (name, surname, cell, email))
        conn.commit()
        conn.close()

        print("Employee has been added!")

    def remove_person(self):
        emp_id = input("\nEnter employee ID to remove: ")

        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("DELETE FROM Employees WHERE `Employee ID`=?", (emp_id))
        conn.commit()
        conn.close()

        print("Employee has been removed!")

    def display_all(self):
        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Employees")
        data = c.fetchall()
        conn.close()

        print("\nEmployees")
        for i in data:
            print(i)
    

# Customer Manager Class
class CustomerManager(PersonManager):
    def insert_person(self):
        name = input("\nEnter customer name: ")
        surname = input("Enter customer surname: ")
        cell = input("Enter customer cell: ")
        email = input("Enter customer email: ")
        address = input("Enter billing address: ")

        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("INSERT INTO Customers (Name, Surname, `Cell Number`, Email, `Billing Address`) VALUES (?, ?, ?, ?, ?)", (name, surname, cell, email, address))
        conn.commit()
        conn.close()

        print("Customer has been added! ")

    def remove_person(self):
        cust_id = input("\nEnter customer ID to remove: ")

        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("DELETE FROM Customers WHERE `Customer ID`=?", (cust_id,))
        conn.commit()
        conn.close()

        print("Customer has been removed!")

    def display_all(self):
        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Customers")
        data = c.fetchall()
        conn.close()

        print("\nCustomers")
        for i in data:
            print(i)

# Store Class
class Store:
    def addProduct(self):
        name = input("\nEnter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("INSERT INTO Products (Name, Price, Quantity) VALUES (?, ?, ?)", (name, price, quantity))
        conn.commit()
        conn.close()

        print("Product has been added!")

    def removeProduct(self):
        prod_id = input("\nEnter product Id to remove: ")

        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("DELETE FROM Products WHERE `Product ID`=?", (prod_id,))
        conn.commit()
        conn.close()

        print("Product has been removed!")

    def updateProduct(self):
        prod_id = input("\nEnter product ID to update: ")
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))

        conn = sqlite3.connect("LondonRoots.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE Products SET Price=?, Quantity=? WHERE `Product ID`=?", (price, quantity, prod_id))
        conn.commit()
        conn.close()

        print("Product has been updated!")

    def displayProduct(self):
        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Products")
        data = c.fetchall()
        conn.close()

        print("\nProducts")
        for i in data:
            print(i)

    def sellProduct(self):
        prod_id = input("\nEnter product ID: ")
        sell_quantity = int(input("Enter quantity to sell: "))

        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("SELECT Name, Price, Quantity FROM Products WHERE `Product ID`=?", (prod_id,))
        
        product = c.fetchone()
        if not product:
            print("Product not found!")
            conn.close()
            return

        name, price, stock = product
        if stock == 0:
            print("Product out of stock!")
            conn.close()
            return

        if sell_quantity > stock:
            print("Not enough stock available!")
            conn.close()
            return

        new_quantity = stock - sell_quantity
        total = sell_quantity * price
        date = datetime.now().strftime("%Y-%m-%d")

        c.execute("UPDATE Products SET Quantity=? WHERE `Product ID`=?", (new_quantity, prod_id))
        c.execute("INSERT INTO Sales (Date, `Product Name`, `Sale Total`) VALUES (?, ?, ?)", (date, name, total))
        conn.commit()
        conn.close()

        print(f"Sale successful! Total = R{total}")

    def displaySales(self):
        conn = sqlite3.connect("LondonRoots.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Sales")
        data = c.fetchall()
        conn.close()

        print("\nSales")
        for i in data:
            print(i)

# Main Method 
def main():

    while True:
        print("\nWelcome to the Store Managment System!")
        print("\n1. Manage Employees")
        print("2. Manage Customers")
        print("3. Manage Products")
        print("4. Manage Sales")
        print("0. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1": 
            employee_manager = EmployeeManager()

            while True:
                print("\n1. Add Employee")
                print("2. Remove Employee")
                print("3. Display Employees")
                print("0. Return to Main Menu")

                choice = input("\nSelect an option: ")
                if choice == "1": 
                    employee_manager.insert_person()

                elif choice == "2": 
                    employee_manager.remove_person()

                elif choice == "3": 
                    employee_manager.display_all()
                
                elif choice == "0":
                    print("Exiting application...")
                    break
                else:
                    print("Invalid choice! Try again.")

        elif choice == "2":
            customer_manager = CustomerManager() 

            while True:
                print("\n1. Add Customer")
                print("2. Remove Customers ")
                print("3. Display Customers")
                print("0. Return to Main Menu")

                choice = input("\nSelect an option: ") 
                if choice == "1": 
                    customer_manager.insert_person()

                elif choice == "2": 
                    customer_manager.remove_person()

                elif choice == "3": 
                    customer_manager.display_all()
                
                elif choice == "0":
                    print("Exiting application...")
                    break
                else:
                    print("Invalid choice! Try again.")

        elif choice == "3":
            store = Store()

            while True:
                print("\n1. Add a Product")
                print("2. Remove a Product")
                print("3. Update a Product")
                print("4. Display a Product")
                print("5. Sell all Product")
                print("0. Return to Main Menu")

                choice = input("\nSelect an option: ")
                if choice == "1": 
                    store.addProduct()

                elif choice == "2": 
                    store.removeProduct()

                elif choice == "3": 
                    store.updateProduct()

                elif choice == "4": 
                    store.displayProduct()
                
                elif choice == "5": 
                    store.sellProduct()
                
                elif choice == "0":
                    print("Exiting application...")
                    break
                else:
                    print("Invalid choice! Try again.")

               
        elif choice == "4": 
            store = Store()

            while True:
                print("\n1. Sell a Product")
                print("2. Display all Sales")
                print("0. Return to Main Menu")

                choice = input("\nSelect an option: ")
                if choice == "1": 
                    store.sellProduct()

                elif choice == "2": 
                    store.displaySales()

                elif choice == "0":
                    print("Exiting application...")
                    break
                else:
                    print("Invalid choice! Try again.")
              
        elif choice == "0":
            print("Exiting application...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()