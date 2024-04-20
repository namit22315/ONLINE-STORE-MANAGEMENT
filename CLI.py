import mysql.connector
from datetime import datetime
from tabulate import tabulate
import os
import time
from tqdm import tqdm
import Admin.Admin_1 as A1
import Admin.Admin_2 as A2
import Admin.Admin_3 as A3
import Admin.Admin_4 as A4
import Admin.Admin_5 as A5
import Admin.Admin_6 as A6
import Admin.Admin_7 as A7
import Admin.Admin_8 as A8
import Admin.Admin_9 as A9
import Admin.Admin_10 as A10
import Admin.Admin_11 as A11
import Admin.Admin_12 as A12
import order_fixer as OFix
import check_products as chkpro
now = datetime.now()
import schedule
import time
dt = now.strftime("%Y-%m-%d %H:%M:%S")

cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()


def clear_screen():
    os.system('clear')


def authenticate_distributor(cursor):
    query = "SELECT distributorID, password FROM Distributor"
    while True:
        distributor_id = int(input("Enter your Distributor ID: "))
        cursor.execute(query)
        distributors = cursor.fetchall()

        for distributor in distributors:
            if distributor_id == distributor[0]:
                print(distributor)
                return distributor

        print("Invalid ID\n")


def verify_password(store):
    while True:
        password = input("Enter your password: ")
        if password == store[1]:
            print("Authenticated")
            return True
        else:
            print("Invalid Password\n")


def main_menu(distributor_id):
    clear_screen()
    print(f"Welcome Distributor ID: {distributor_id}")
    print("---------------------------------------------")
    print("Please choose a number from the menu to proceed:")
    menu = {"Number": ['1', '2', '3'],
            "Task": ["View Products you Distribute", "Add a New Product", "Exit to Main Menu"]}
    print(tabulate(menu, headers='keys', tablefmt='fancy_grid'))

def view_product(id_dist):
    query_view_dist = f"""
                            SELECT Distributor.distributorID, Distributor.productID, Product.productID, Product.name
                            FROM
                            Distributor, Product
                            WHERE 
                            Distributor.productID = Product.productID
                            AND
                            Distributor.distributorID = {id_dist}
                            """
    prod_id = []
    prod_name = []
    cursor.execute(query_view_dist)
    for row in cursor.fetchall():
        prod_id.append(row[2])
        prod_name.append(row[3])
    table_prod_dist = {"Product ID": prod_id,
                       "Product Name": prod_name}
    print(tabulate(table_prod_dist, headers='keys', tablefmt='fancy_grid'))
    print('\n')

def add_new_product(id_dist):
    prod_id_new = int(input("Enter the Product ID of the Product you want to add: "))
    query_prod_name = f"""
                            SELECT Product.productID, Product.name
                            FROM 
                            Product
                            WHERE
                            Product.productID = {prod_id_new}"""
    name = ''
    cursor.execute(query_prod_name)
    for row in cursor.fetchall():
        name = row[1]
    query_id_exist = f"""
                            SELECT Distributor.distributorID, Distributor.productID
                            FROM
                            Distributor
                            WHERE 
                            Distributor.distributorID = {id_dist}
                            """
    cursor.execute(query_id_exist)
    exist = 0
    for row in cursor.fetchall():
        if (row[1] == prod_id_new):
            exist = 1
            break
    if (exist):
        print("Sorry cannot add this product, you are already a distributor")
    else:
        dist_deets = f"""
                                SELECT * 
                                FROM 
                                Distributor
                                WHERE 
                                Distributor.distributorID = {id_dist}"""
        cursor.execute(dist_deets)
        for row in cursor.fetchall():
            one = row[0]
            two = row[1]
            three = row[3]
            four = row[4]
            five = row[5]
            six = row[6]
            seven = row[7]
            eight = row[8]
            nine = row[9]
        query_add_dist = "insert into Distributor (distributorID, password, productID, phone_number, email_address, commission, house_number, street_name, city, pincode) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        val = (one, two, prod_id_new, three, four, five, six, seven, eight, nine)
        cursor.execute(query_add_dist, val)
        cnx.commit()
        print(f"\n Successfully Added {name} \n")

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and MacOS
    else:
        os.system('clear')


def bill_customer(val):
    try:
        cnx.autocommit = False
        query_insert = """insert into Billing (payment_mode, bill_amount, amount_donated, orderID, ngoID) values (%s, %s, %s, %s, %s)"""
        cursor.execute(query_insert, val)
        cnx.commit()
    except Exception as e:
        print(e)
        cnx.rollback()
        print("Error billing customer.")


print("""
          _____                    _____                   _______                   _____                    _____                    _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                 /::\    \                 /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \               /::::\    \               /::\    \                /::\    \                /::\    \                /::\    \                /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \             /::::::\    \             /::::\    \              /::::\    \              /::::\    \              /::::\    \              /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \           /::::::::\    \           /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \         /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \       /:::/    \:::\    \       /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \     /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \       \:::\   \:::\    \      /::::\   \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\   /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    ___\:::\   \:::\    \    /::::::\   \:::\    \  
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\____\ |:::|    |     |:::|    | /:::/    /   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \ 
/:::/____/  ___\:::|    |/:::/  \:::\   \:::|    ||:::|____|     |:::|    |/:::/____/     \:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/__\:::\   \:::\____\/:::/  \:::\   \:::\____\/::\   \:::\   \:::\____\/:::/__\:::\   \:::\____\/
\:::\    \ /\  /:::|____|\::/   |::::\  /:::|____| \:::\    \   /:::/    / \:::\    \      \::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /
 \:::\    /::\ \::/    /  \/____|:::::\/:::/    /   \:::\    \ /:::/    /   \:::\    \      \/____/  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /  \:::\   \:::\   \/____/  \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/ 
  \:::\   \:::\ \/____/         |:::::::::/    /     \:::\    /:::/    /     \:::\    \               \:::\   \:::\    \            |:::::::::/    /    \:::\   \:::\    \               \::::::/    /    \:::\   \:::\    \       \:::\   \:::\    \     
   \:::\   \:::\____\           |::|\::::/    /       \:::\__/:::/    /       \:::\    \               \:::\   \:::\____\           |::|\::::/    /      \:::\   \:::\____\               \::::/    /      \:::\   \:::\____\       \:::\   \:::\____\    
    \:::\  /:::/    /           |::| \::/____/         \::::::::/    /         \:::\    \               \:::\   \::/    /           |::| \::/____/        \:::\   \::/    /               /:::/    /        \:::\  /:::/    /        \:::\   \::/    /    
     \:::\/:::/    /            |::|  ~|                \::::::/    /           \:::\    \               \:::\   \/____/            |::|  ~|               \:::\   \/____/               /:::/    /          \:::\/:::/    /          \:::\   \/____/     
      \::::::/    /             |::|   |                 \::::/    /             \:::\    \               \:::\    \                |::|   |                \:::\    \                  /:::/    /            \::::::/    /            \:::\    \         
       \::::/    /              \::|   |                  \::/____/               \:::\____\               \:::\____\               \::|   |                 \:::\____\                /:::/    /              \::::/    /              \:::\____\        
        \::/____/                \:|   |                   ~~                      \::/    /                \::/    /                \:|   |                  \::/    /                \::/    /                \::/    /                \::/    /        
                                  \|___|                                            \/____/                  \/____/                  \|___|                   \/____/                  \/____/                  \/____/                  \/____/         

""")
print("Starting online retail store...")
duration = 5

# Increment duration (you can adjust the sleep time to make the bar smoother or more granular)
sleep_time = 0.1

# Total iterations to complete in the given duration
total_iterations = int(duration / sleep_time)

# Create the progress bar using tqdm
for _ in tqdm(range(total_iterations), desc="Processing"):
    time.sleep(sleep_time)

print("Done!")
print("Starting initial health restore...")
for _ in tqdm(range(total_iterations), desc="Processing"):
    time.sleep(sleep_time)

OFix.job()
print("Checking product discrepancies...")
for _ in tqdm(range(total_iterations), desc="Processing"):
    time.sleep(sleep_time)
chkpro.job()


print("Done!")
while True:
    print("\n\n\n\n")
    print("Welcome to the Online Retail Store")
    print("---------------------------------------------")
    print("Please choose a number from the menu to proceed: ")
    table_main_menu = [['Number', 'Task'], ['1', 'Admin LogIn'],
                       ['2', 'User LogIn'],
                       ['3', 'User SignUp'],
                       ['4', 'Distributor LogIn'],
                       ['5', 'NGO Data'],
                       ['6', 'Exit']]
    print(tabulate(table_main_menu, headers='firstrow', tablefmt="fancy_grid"))

    input_1 = int(input("Enter the number from the menu: "))
    # ADMIN LOGIN
    clear_terminal()
    if input_1 == 1:
        print("""
          _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\                /::\    \                /::\____\        
       /::::\    \              /::::\    \              /::::|   |                \:::\    \              /::::|   |        
      /::::::\    \            /::::::\    \            /:::::|   |                 \:::\    \            /:::::|   |        
     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |                  \:::\    \          /::::::|   |        
    /:::/__\:::\    \        /:::/  \:::\    \        /:::/|::|   |                   \:::\    \        /:::/|::|   |        
   /::::\   \:::\    \      /:::/    \:::\    \      /:::/ |::|   |                   /::::\    \      /:::/ |::|   |        
  /::::::\   \:::\    \    /:::/    / \:::\    \    /:::/  |::|___|______    ____    /::::::\    \    /:::/  |::|   | _____  
 /:::/\:::\   \:::\    \  /:::/    /   \:::\ ___\  /:::/   |::::::::\    \  /\   \  /:::/\:::\    \  /:::/   |::|   |/\    \ 
/:::/  \:::\   \:::\____\/:::/____/     \:::|    |/:::/    |:::::::::\____\/::\   \/:::/  \:::\____\/:: /    |::|   /::\____\/
\::/    \:::\  /:::/    /\:::\    \     /:::|____|\::/    / ~~~~~/:::/    /\:::\  /:::/    \::/    /\::/    /|::|  /:::/    /
 \/____/ \:::\/:::/    /  \:::\    \   /:::/    /  \/____/      /:::/    /  \:::\/:::/    / \/____/  \/____/ |::| /:::/    / 
          \::::::/    /    \:::\    \ /:::/    /               /:::/    /    \::::::/    /                   |::|/:::/    /  
           \::::/    /      \:::\    /:::/    /               /:::/    /      \::::/____/                    |::::::/    /   
           /:::/    /        \:::\  /:::/    /               /:::/    /        \:::\    \                    |:::::/    /    
          /:::/    /          \:::\/:::/    /               /:::/    /          \:::\    \                   |::::/    /     
         /:::/    /            \::::::/    /               /:::/    /            \:::\    \                  /:::/    /      
        /:::/    /              \::::/    /               /:::/    /              \:::\____\                /:::/    /       
        \::/    /                \::/____/                \::/    /                \::/    /                \::/    /        
         \/____/                  ~~                       \/____/                  \/____/                  \/____/         

""")
        print("\n---------------------------------------------\n")
        count = 0
        valid_admin = 0
        username = ''
        while count < 3 and valid_admin == 0:
            query_auth_admin = """ Select username,password from Admin"""
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            cursor.execute(query_auth_admin)
            for row in cursor.fetchall():
                if username == row[0] and password == row[1]:
                    # store = row
                    # print(row)
                    valid_admin = 1
                    print("Authenticated\n")
                    break
            if valid_admin == 0:
                print("Invalid Username or password\n")
                count += 1
                print(f"{3 - count} tries remaining\n")

        while valid_admin:
            print(f"\nWelcome {username}")
            table_admin_menu = {
                'Number': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13','14'],
                'Task': ['View Quarterly Sales of the each Category',
                         'View Curated Sales Data for Each Category',
                         'View Top 5 Customers(based on money spent)',
                         'Data of items in the Inventory for each storage type',
                         'Add Category',
                         'View All Category',
                         'View Ratings of Top 10 Delivery Partner and Wages',
                         'View Incomplete Orders and Status',
                         'View Products and Change Quantity in Inventory',
                         'Assign a Delivery Partner to Deliver Order',
                         'Add Product to Inventory',
                         'remove a Product from Inventory',
                         'run automated tests',
                         'Log Out']
            }
            print(tabulate(table_admin_menu, headers='keys', tablefmt="fancy_grid"))
            input_admin = int(input("Enter the number from the menu: "))
            if input_admin == 1:
                A1.get_quarterly_sales()
            elif input_admin == 2:
                A2.get_curated_sales_data()
            # Number of Distinct Customers: {row[4]}
            elif input_admin == 3:
                A3.get_top_customers()
            elif input_admin == 4:
                inventory_data = A4.get_inventory_items()

                table = []
                for row in inventory_data:
                    table.append([row[0], row[1]])

                print(tabulate(table, headers=["Storage Type", "Items"], tablefmt="fancy_grid"))

            elif input_admin == 5:
                A5.add_category()

            elif input_admin == 6:
                A6.view_category()

            elif input_admin == 7:
                A7.view_top_delivery_partners()

            elif input_admin == 8:
                A8.view_incomplete_orders()

            elif input_admin == 9:
                A9.view_and_update_inventory()

            elif input_admin == 10:
                inp = int(input("assign delivery partner"))
                A10.assign_delivery_partner(inp)

            elif input_admin == 11:
                new_category_id = input("Enter category ID: ")
                new_product_name = input("Enter product: ")
                new_product_quantity = input("Enter quantity of product: ")
                new_product_price = input("Enter price of product: ")
                new_product_discount = input("Enter discount: ")
                new_product_storage_type = input("Enter storage type: ")
                new_product_rating = input("Enter rating: ")
                new_product_description = input("Enter description: ")
                warehouseID = input("Enter Warehouse ID: ")
                A11.add_product(new_category_id, new_product_name, new_product_quantity,
                                new_product_price,
                                new_product_discount, new_product_storage_type, new_product_rating,
                                new_product_description, warehouseID)

            elif input_admin == 12:
                product_id_to_remove = int(input("Enter the product ID to remove from the Product table: "))

                A12.remove_product(product_id_to_remove)
            elif input_admin == 13:

                def job():
                    print("Running inventory check...")
                    OFix.job()
                    chkpro.job()


                schedule.every(10).seconds.do(job)

                # Keep the script running in a loop
                while True:
                    schedule.run_pending()
                    time.sleep(1)


            elif input_admin == 14:
                break
            else:
                print("Invalid Input!")

    # USER LOGIN
    elif input_1 == 2:
        print("""
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\    \                /::\    \        
       /:::/    /               /::::\    \              /::::\    \              /::::\    \       
      /:::/    /               /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/    /               /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/    /               /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /:::/    /                \:::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  /:::/    /      _____    ___\:::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/____/      /\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
|:::|    /      /::\____\/::\   \:::\   \:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |
|:::|____\     /:::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|
 \:::\    \   /:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \/____|:::::\/:::/    / 
  \:::\    \ /:::/    /    \:::\   \:::\    \       \:::\   \:::\    \            |:::::::::/    /  
   \:::\    /:::/    /      \:::\   \:::\____\       \:::\   \:::\____\           |::|\::::/    /   
    \:::\__/:::/    /        \:::\  /:::/    /        \:::\   \::/    /           |::| \::/____/    
     \::::::::/    /          \:::\/:::/    /          \:::\   \/____/            |::|  ~|          
      \::::::/    /            \::::::/    /            \:::\    \                |::|   |          
       \::::/    /              \::::/    /              \:::\____\               \::|   |          
        \::/____/                \::/    /                \::/    /                \:|   |          
         ~~                       \/____/                  \/____/                  \|___|          

""")
        print("\n----------------------------------------------\n")
        count = 0
        valid_user = 0
        username = ''
        while count < 3 and valid_user == 0:
            query_auth_user = """Select username,password from Customer"""
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            cursor.execute(query_auth_user)
            for row in cursor.fetchall():
                if username == row[0] and password == row[1]:
                    # store = row
                    # print(row)
                    valid_user = 1
                    print("Authenticated\n")
                    break
            if valid_user == 0:
                print("Invalid Username or password\n")
                count += 1
                print(f"{3 - count} tries remaining\n")
        while valid_user:
            print(f"Welcome {username}")
            print("---------------------------------------------")
            print("Please choose a number from the menu to proceed: ")
            table_user = {'Number': ['1', '2', '3', '4', '5'],
                          'Task': ['Add Products to Cart', 'View Cart', 'Proceed To CheckOut',
                                   'View Order History', 'Exit To Main Menu']}
            print(tabulate(table_user, headers='keys', tablefmt='fancy_grid'))
            input_user = int(input("Enter the number from the menu: "))
            if input_user == 1:
                query = " SELECT category_name FROM Category"
                cursor.execute(query)
                i = 1
                print(f"Select from the given categories or type exit to exit the menu: ")
                for row in cursor.fetchall():
                    print(f"{i}: {row[0]}")
                    i += 1
                inp_customer = input()

                if inp_customer != 'exit':
                    inp_category = int(inp_customer)
                    query2 = f"""
                    SELECT Product.productID, Product.name, Product.categoryID, Product.price
                    FROM Category
                    JOIN Product ON Product.categoryID = Category.categoryID
                    WHERE Product.categoryID = {inp_category}
                    GROUP BY Product.productID
                    ORDER BY Product.productID ASC
                    """
                    cursor.execute(query2)
                    for row in cursor.fetchall():
                        print(f"{row[0]}: {row[1]}")
                    inp_id_choice = input("Enter the id of the product you want to add to cart or type exit: ")
                    if inp_id_choice != 'exit':
                        inp_id = int(inp_id_choice)
                        try:
                            cnx.autocommit = False
                            check_quantity_query = f"SELECT quantity FROM Inventory WHERE productID = {inp_id}"
                            cursor.execute(check_quantity_query)
                            current_quantity = cursor.fetchone()[0]
                            num = int(input("Enter quantity: "))
                            if (current_quantity >= num):
                                update_query = f"UPDATE Inventory SET quantity = {current_quantity - num} WHERE productID = {inp_id}"
                                cursor.execute(update_query)
                                update_prod = f"UPDATE Product SET quantity_in_stock = {current_quantity - num} WHERE productID = {inp_id}"
                                cursor.execute(update_prod)
                                query_3 = f"""
                                SELECT Product.productID, Product.name, Product.price
                                FROM Product
                                WHERE Product.productID = {inp_id}
                                """
                                un = username
                                cursor.execute(query_3)
                                product_details = cursor.fetchone()
                                id = product_details[0]
                                cost = product_details[2]
                                check_cart_query = f"""
                                SELECT CartID, quantity
                                FROM Cart
                                WHERE username = '{username}' AND productID = {id}
                                """
                                cursor.execute(check_cart_query)
                                cart_entry = cursor.fetchone()
                                if cart_entry:
                                    cart_id, existing_quantity = cart_entry
                                    new_quantity = existing_quantity + num
                                    update_cart_query = f"UPDATE Cart SET quantity = {new_quantity}, billing_amount = {cost * new_quantity} WHERE CartID = {cart_id} AND productID = {id}"
                                    cursor.execute(update_cart_query)
                                else:
                                    query_cart = """
                                    INSERT INTO Cart (billing_amount, productID, quantity, username)
                                    VALUES (%s, %s, %s, %s)
                                    """
                                    val = (cost * num, id, num, username)
                                    cursor.execute(query_cart, val)
                                cnx.commit()
                            else:
                                print(f"Not enough quantity in stock for product.")
                        except Exception as e:
                            print(f"Error: {e}")
                            cnx.rollback()

            elif input_user == 2:
                query_view_cart = f"""
                select 
                Cart.quantity, Cart.billing_amount, Product.productID, Product.name, Cart.productID, Cart.username 
                from 
                Product, Cart 
                where 
                Product.productID = Cart.productID"""
                cursor.execute(query_view_cart)
                bill = 0
                for row in cursor.fetchall():
                    if row[5] == username:
                        if row[0] != 0:
                            print(f"item name: {row[3]}, quantity: {row[0]}")
                        bill += row[1]
                print(f"billing amount: {bill}")

            elif input_user == 3:
                print("Items that are present in your cart: ")
                query_view_cart = f"""
                SELECT 
                Cart.quantity, Cart.billing_amount, Product.productID, Product.name, Cart.productID, Cart.username 
                from 
                Product, Cart 
                where 
                Product.productID = Cart.productID"""

                last_id = """
                SELECT orderID 
                FROM `Order`
                ORDER BY orderID DESC
                LIMIT 1
                """
                id_l = 0
                cursor.execute(last_id)
                for row in cursor.fetchall():
                    id_l = row[0]
                print(id_l)
                bill_amount = bill
                print(
                    "Plz donate some amount to our tie-up NGOs and support humanity! If you don't want to donate, "
                    "enter amount as 0.")
                query_ngo = f"""select NGO.ngoID, NGO.name from NGO"""
                cursor.execute(query_ngo)
                for row in cursor.fetchall():
                    print(f"NGO ID: {row[0]}, NGO Name: {row[1]}")
                ngo_id = int(input())
                amount_donated = round(float(input("Amount to donate : ")), 2)
                method_to_pay = input("Method to pay (COD/UPI/card/wallet) : ")
                cursor.execute(query_view_cart)
                for row in cursor.fetchall():
                    if row[5] == username:
                        print(f"item name: {row[3]}, quantity: {row[0]}")
                        bill = row[1]
                        query_insert = """insert into `Order` (username, status, order_amount, discount, 
                        date_order_placed) values (%s, %s, %s, %s, %s)"""
                        query_remove_cart = f"""
                        DELETE FROM 
                        Cart 
                        WHERE 
                        username = '{str(username)}'
                        """
                        now = datetime.now()
                        dt = now.strftime("%Y-%m-%d %H:%M:%S")
                        val = (username, 'order_placed', round(float(bill), 2), 0, dt)
                        cursor.execute(query_insert, val)
                        cursor.execute(query_remove_cart)
                        cnx.commit()
                query_insertt = """insert into Cart (billing_amount, quantity, username) values (%s,%s,%s)"""
                val = (0, 0, username)
                cursor.execute(query_insertt, val)
                cnx.commit()
                val = (method_to_pay, round(float(bill_amount), 2), amount_donated, id_l, ngo_id)
                bill_customer(val)

            elif input_user == 4:
                query_hist = f"""
                SELECT `Order`.username, `Order`.status, `Order`.order_amount, `Order`.discount , `Order`.orderID, `Order`.date_order_placed
                FROM `Order`
                WHERE
                `Order`.username = '{str(username)}'
                """
                cursor.execute(query_hist)
                stat = []
                amo = []
                order_id = []
                date = []
                for row in cursor.fetchall():
                    order_id.append(row[4])
                    stat.append(row[1])
                    amo.append(row[2])
                    date.append(row[5])
                table_order_hist = {"Order ID": order_id,
                                    "Status": stat,
                                    "Amount": amo,
                                    "Date_order_placed": date}
                print(tabulate(table_order_hist, headers='keys', tablefmt='fancy_grid'))
            elif input_user == 5:
                break
            else:
                print("Invalid Input!")

    elif input_1 == 3:
        print("""
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\    \                /::\    \        
       /:::/    /               /::::\    \              /::::\    \              /::::\    \       
      /:::/    /               /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/    /               /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/    /               /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /:::/    /                \:::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  /:::/    /      _____    ___\:::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/____/      /\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
|:::|    /      /::\____\/::\   \:::\   \:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |
|:::|____\     /:::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|
 \:::\    \   /:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \/____|:::::\/:::/    / 
  \:::\    \ /:::/    /    \:::\   \:::\    \       \:::\   \:::\    \            |:::::::::/    /  
   \:::\    /:::/    /      \:::\   \:::\____\       \:::\   \:::\____\           |::|\::::/    /   
    \:::\__/:::/    /        \:::\  /:::/    /        \:::\   \::/    /           |::| \::/____/    
     \::::::::/    /          \:::\/:::/    /          \:::\   \/____/            |::|  ~|          
      \::::::/    /            \::::::/    /            \:::\    \                |::|   |          
       \::::/    /              \::::/    /              \:::\____\               \::|   |          
        \::/____/                \::/    /                \::/    /                \:|   |          
         ~~                       \/____/                  \/____/                  \|___|          

""")
        print("\n-----------------------------------------------\n")
        print("User SignUp")
        username = input("Set your username: ")
        password = input("Set your password: ")
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        phone = input("Enter phone number: ")
        mail = input("Enter email id: ")
        h_no = int(input("Enter house number: "))
        street = input("Enter street name: ")
        city = input("Enter city: ")
        zone = input("Enter zone: ")
        pin = int(input("Enter 6 digit pin code: "))
        query_insert = """insert into Customer (username, password, first_name, last_name, phone_number, 
        house_number,street_name, city, zone, pincode) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        val = (username, password, f_name, l_name, phone, h_no, street, city, zone, pin)
        cursor.execute(query_insert, val)
        cnx.commit()
        query_insert = """insert into Cart (billing_amount, quantity, username) values (%s,%s,%s)"""
        val = (0, 0, username)
        cursor.execute(query_insert, val)
        cnx.commit()
        print('Successful SignUp')
        print("Redirecting to Home Page")
    elif input_1 == 4:
        print("""
          _____                    _____                    _____                _____                    _____                    _____                    _____                    _____                _____                   _______                   _____          
         /\    \                  /\    \                  /\    \              /\    \                  /\    \                  /\    \                  /\    \                  /\    \              /\    \                 /::\    \                 /\    \         
        /::\    \                /::\    \                /::\    \            /::\    \                /::\    \                /::\    \                /::\    \                /::\____\            /::\    \               /::::\    \               /::\    \        
       /::::\    \               \:::\    \              /::::\    \           \:::\    \              /::::\    \               \:::\    \              /::::\    \              /:::/    /            \:::\    \             /::::::\    \             /::::\    \       
      /::::::\    \               \:::\    \            /::::::\    \           \:::\    \            /::::::\    \               \:::\    \            /::::::\    \            /:::/    /              \:::\    \           /::::::::\    \           /::::::\    \      
     /:::/\:::\    \               \:::\    \          /:::/\:::\    \           \:::\    \          /:::/\:::\    \               \:::\    \          /:::/\:::\    \          /:::/    /                \:::\    \         /:::/~~\:::\    \         /:::/\:::\    \     
    /:::/  \:::\    \               \:::\    \        /:::/__\:::\    \           \:::\    \        /:::/__\:::\    \               \:::\    \        /:::/__\:::\    \        /:::/    /                  \:::\    \       /:::/    \:::\    \       /:::/__\:::\    \    
   /:::/    \:::\    \              /::::\    \       \:::\   \:::\    \          /::::\    \      /::::\   \:::\    \              /::::\    \      /::::\   \:::\    \      /:::/    /                   /::::\    \     /:::/    / \:::\    \     /::::\   \:::\    \   
  /:::/    / \:::\    \    ____    /::::::\    \    ___\:::\   \:::\    \        /::::::\    \    /::::::\   \:::\    \    ____    /::::::\    \    /::::::\   \:::\    \    /:::/    /      _____        /::::::\    \   /:::/____/   \:::\____\   /::::::\   \:::\    \  
 /:::/    /   \:::\ ___\  /\   \  /:::/\:::\    \  /\   \:::\   \:::\    \      /:::/\:::\    \  /:::/\:::\   \:::\____\  /\   \  /:::/\:::\    \  /:::/\:::\   \:::\ ___\  /:::/____/      /\    \      /:::/\:::\    \ |:::|    |     |:::|    | /:::/\:::\   \:::\____\ 
/:::/____/     \:::|    |/::\   \/:::/  \:::\____\/::\   \:::\   \:::\____\    /:::/  \:::\____\/:::/  \:::\   \:::|    |/::\   \/:::/  \:::\____\/:::/__\:::\   \:::|    ||:::|    /      /::\____\    /:::/  \:::\____\|:::|____|     |:::|    |/:::/  \:::\   \:::|    |
\:::\    \     /:::|____|\:::\  /:::/    \::/    /\:::\   \:::\   \::/    /   /:::/    \::/    /\::/   |::::\  /:::|____|\:::\  /:::/    \::/    /\:::\   \:::\  /:::|____||:::|____\     /:::/    /   /:::/    \::/    / \:::\    \   /:::/    / \::/   |::::\  /:::|____|
 \:::\    \   /:::/    /  \:::\/:::/    / \/____/  \:::\   \:::\   \/____/   /:::/    / \/____/  \/____|:::::\/:::/    /  \:::\/:::/    / \/____/  \:::\   \:::\/:::/    /  \:::\    \   /:::/    /   /:::/    / \/____/   \:::\    \ /:::/    /   \/____|:::::\/:::/    / 
  \:::\    \ /:::/    /    \::::::/    /            \:::\   \:::\    \      /:::/    /                 |:::::::::/    /    \::::::/    /            \:::\   \::::::/    /    \:::\    \ /:::/    /   /:::/    /             \:::\    /:::/    /          |:::::::::/    /  
   \:::\    /:::/    /      \::::/____/              \:::\   \:::\____\    /:::/    /                  |::|\::::/    /      \::::/____/              \:::\   \::::/    /      \:::\    /:::/    /   /:::/    /               \:::\__/:::/    /           |::|\::::/    /   
    \:::\  /:::/    /        \:::\    \               \:::\  /:::/    /    \::/    /                   |::| \::/____/        \:::\    \               \:::\  /:::/    /        \:::\__/:::/    /    \::/    /                 \::::::::/    /            |::| \::/____/    
     \:::\/:::/    /          \:::\    \               \:::\/:::/    /      \/____/                    |::|  ~|               \:::\    \               \:::\/:::/    /          \::::::::/    /      \/____/                   \::::::/    /             |::|  ~|          
      \::::::/    /            \:::\    \               \::::::/    /                                  |::|   |                \:::\    \               \::::::/    /            \::::::/    /                                  \::::/    /              |::|   |          
       \::::/    /              \:::\____\               \::::/    /                                   \::|   |                 \:::\____\               \::::/    /              \::::/    /                                    \::/____/               \::|   |          
        \::/____/                \::/    /                \::/    /                                     \:|   |                  \::/    /                \::/____/                \::/____/                                      ~~                      \:|   |          
         ~~                       \/____/                  \/____/                                       \|___|                   \/____/                  ~~                       ~~                                                                     \|___|          

""")
        print("\n---------------------------------------------\n")
        # distributor_console();
        while (True):
            query_auth_dist = """Select distributorID, password from Distributor"""
            id_dist = int(input("Enter your Distributor ID: "))
            cursor.execute(query_auth_dist)
            valid_user = 0
            for row in cursor.fetchall():
                if (id_dist) == row[0]:
                    store = row
                    print(row)
                    valid_user = 1
                    break
            if valid_user:
                break
            else:
                print("Invalid ID\n")

        while (True):
            password = input("Enter your password: ")
            if password in store:
                print("Authenticated")
                valid_dist = 1
                break
            else:
                print("Invalid Password \n")
        while (valid_dist):
            print(f"Welcome Distributor ID : {id_dist}")
            print("---------------------------------------------")
            print("Please choose a number from the menu to proceed: ")
            table_distributor = {"Number": ['1', '2', '3'],
                                 "Task": ["View Products you Distribute",
                                          "Add a New Product",
                                          "Exit to Main Menu"]}
            print(tabulate(table_distributor, headers='keys', tablefmt='fancy_grid'))
            input_dist = int(input("Enter the number from the menu: "))
            if (input_dist == 1):
                view_product(id_dist)
            elif (input_dist == 2):
                add_new_product(id_dist)

            elif (input_dist == 3):
                break
    elif input_1 == 5:
        print("""
          _____                    _____                   _______         
         /\    \                  /\    \                 /::\    \        
        /::\____\                /::\    \               /::::\    \       
       /::::|   |               /::::\    \             /::::::\    \      
      /:::::|   |              /::::::\    \           /::::::::\    \     
     /::::::|   |             /:::/\:::\    \         /:::/~~\:::\    \    
    /:::/|::|   |            /:::/  \:::\    \       /:::/    \:::\    \   
   /:::/ |::|   |           /:::/    \:::\    \     /:::/    / \:::\    \  
  /:::/  |::|   | _____    /:::/    / \:::\    \   /:::/____/   \:::\____\ 
 /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\ |:::|    |     |:::|    |
/:: /    |::|   /::\____\/:::/____/  ___\:::|    ||:::|____|     |:::|    |
\::/    /|::|  /:::/    /\:::\    \ /\  /:::|____| \:::\    \   /:::/    / 
 \/____/ |::| /:::/    /  \:::\    /::\ \::/    /   \:::\    \ /:::/    /  
         |::|/:::/    /    \:::\   \:::\ \/____/     \:::\    /:::/    /   
         |::::::/    /      \:::\   \:::\____\        \:::\__/:::/    /    
         |:::::/    /        \:::\  /:::/    /         \::::::::/    /     
         |::::/    /          \:::\/:::/    /           \::::::/    /      
         /:::/    /            \::::::/    /             \::::/    /       
        /:::/    /              \::::/    /               \::/____/        
        \::/    /                \::/____/                 ~~              
         \/____/                                                           

""")
        print("\n---------------------------------------------\n")
        # print("under construction")
        ngo_funds = f"""select * from NGO"""
        cursor.execute(ngo_funds)
        ngo_id = []
        ngo_name = []
        reg_num = []
        funds = []
        for row in cursor.fetchall():
            ngo_id.append(row[0])
            ngo_name.append(row[1])
            reg_num.append(row[2])
            funds.append(row[4])
        table_ngo = {'NGO ID': ngo_id,
                     'Name of NGO': ngo_name,
                     'Registeration Number': reg_num,
                     'Funds Raised': funds
                     }
        print(tabulate(table_ngo, headers='keys', tablefmt='fancy_grid'))

        go_back = int(input('Press 1 to go back to main screen: '))
        while (go_back != 1):
            continue

    elif input_1 == 6:
        print("""
      _____                    _____                    _____                    _____                    _____                        _____                   _______                   _____          
     /\    \                  /\    \                  /\    \                  /\    \                  /\    \                      |\    \                 /::\    \                 /\    \         
    /::\    \                /::\____\                /::\    \                /::\____\                /::\____\                     |:\____\               /::::\    \               /::\____\        
    \:::\    \              /:::/    /               /::::\    \              /::::|   |               /:::/    /                     |::|   |              /::::::\    \             /:::/    /        
     \:::\    \            /:::/    /               /::::::\    \            /:::::|   |              /:::/    /                      |::|   |             /::::::::\    \           /:::/    /         
      \:::\    \          /:::/    /               /:::/\:::\    \          /::::::|   |             /:::/    /                       |::|   |            /:::/~~\:::\    \         /:::/    /          
       \:::\    \        /:::/____/               /:::/__\:::\    \        /:::/|::|   |            /:::/____/                        |::|   |           /:::/    \:::\    \       /:::/    /           
       /::::\    \      /::::\    \              /::::\   \:::\    \      /:::/ |::|   |           /::::\    \                        |::|   |          /:::/    / \:::\    \     /:::/    /            
      /::::::\    \    /::::::\    \   _____    /::::::\   \:::\    \    /:::/  |::|   | _____    /::::::\____\________               |::|___|______   /:::/____/   \:::\____\   /:::/    /      _____  
     /:::/\:::\    \  /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/\:::::::::::\    \              /::::::::\    \ |:::|    |     |:::|    | /:::/____/      /\    \ 
    /:::/  \:::\____\/:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\/:::/  |:::::::::::\____\            /::::::::::\____\|:::|____|     |:::|    ||:::|    /      /::\____\/
   /:::/    \::/    /\::/    \:::\  /:::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /\::/   |::|~~~|~~~~~                /:::/~~~~/~~       \:::\    \   /:::/    / |:::|____\     /:::/    /
  /:::/    / \/____/  \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    /  \/____|::|   |                    /:::/    /           \:::\    \ /:::/    /   \:::\    \   /:::/    / 
 /:::/    /                    \::::::/    /            \::::::/    /           |::|/:::/    /         |::|   |                   /:::/    /             \:::\    /:::/    /     \:::\    \ /:::/    /  
/:::/    /                      \::::/    /              \::::/    /            |::::::/    /          |::|   |                  /:::/    /               \:::\__/:::/    /       \:::\    /:::/    /   
\::/    /                       /:::/    /               /:::/    /             |:::::/    /           |::|   |                  \::/    /                 \::::::::/    /         \:::\__/:::/    /    
 \/____/                       /:::/    /               /:::/    /              |::::/    /            |::|   |                   \/____/                   \::::::/    /           \::::::::/    /     
                              /:::/    /               /:::/    /               /:::/    /             |::|   |                                              \::::/    /             \::::::/    /      
                             /:::/    /               /:::/    /               /:::/    /              \::|   |                                               \::/____/               \::::/    /       
                             \::/    /                \::/    /                \::/    /                \:|   |                                                ~~                      \::/____/        
                              \/____/                  \/____/                  \/____/                  \|___|                                                                         ~~              

""")
        print("\n\n")
        break
    else:
        print("Sorry, invalid number")
        print("Please try again\n")
cnx.close()
if cnx:
    cnx.close()
