import mysql.connector
from datetime import datetime, timedelta
from tabulate import tabulate
cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()

def get_top_customers():
    # Query to get the top 5 customers based on money spent
    query = """
        SELECT c.username, c.first_name, c.last_name, SUM(b.bill_amount) AS total_spent
        FROM Customer c
        JOIN `Order` o ON c.username = o.username
        JOIN Billing b ON o.orderID = b.orderID
        GROUP BY c.username, c.first_name, c.last_name
        ORDER BY total_spent DESC
        LIMIT 5
    """
    cursor.execute(query)
    results = cursor.fetchall()

    rows = []
    for row in results:
        username, first_name, last_name, total_spent = row
        rows.append([username, first_name, last_name, f"${total_spent:.2f}"])

    print(tabulate(rows, headers=["Username", "First Name", "Last Name", "Total Spent"], tablefmt="fancy_grid"))
