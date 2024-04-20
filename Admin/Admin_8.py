import mysql.connector

from tabulate import tabulate
import mysql.connector
from datetime import datetime, timedelta
cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()


def view_incomplete_orders():
    # Query to fetch incomplete orders
    query = """
    SELECT o.orderID, c.username, c.first_name, c.last_name, o.status, o.order_amount, o.date_order_placed
    FROM `Order` o
    JOIN Customer c ON o.username = c.username
    WHERE o.status IN ('Processing', 'Shipped')
    ORDER BY o.date_order_placed DESC;
    """

    cursor.execute(query)

    # Prepare the data for tabulation
    rows = []
    for row in cursor:
        order_id, username, first_name, last_name, status, order_amount, order_date = row
        rows.append([order_id, f"{first_name} {last_name}", status, f"${order_amount:.2f}", order_date])

    # Print the results in a fancy grid format
    print("Incomplete Orders:")
    print(tabulate(rows, headers=["Order ID", "Customer Name", "Status", "Order Amount", "Order Date"], tablefmt="fancy_grid"))
