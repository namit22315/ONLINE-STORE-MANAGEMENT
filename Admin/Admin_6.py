import mysql.connector

from tabulate import tabulate
import mysql.connector
from datetime import datetime, timedelta
cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()

def view_category():
    """Function to view category table including category ID, name, and discount, formatted in a fancy grid style."""


    # SQL query to fetch category details
    query = "SELECT categoryID, category_name, category_discount FROM category;"
    cursor.execute(query)

    # Fetch all the rows
    results = cursor.fetchall()

    # Define the table headers
    headers = ["Category ID", "Category Name", "Category Discount"]

    # Print the table
    print(tabulate(results, headers=headers, tablefmt="fancy_grid"))



