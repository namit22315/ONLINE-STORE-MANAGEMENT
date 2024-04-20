import mysql.connector

from tabulate import tabulate
import mysql.connector
from datetime import datetime, timedelta
cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()

def view_top_delivery_partners():
    print("Top 10 Delivery Partners by Rating:")
    query = """
    SELECT first_name, last_name, rating, salary
    FROM DeliveryPartner
    WHERE rating IS NOT NULL
    ORDER BY rating DESC
    LIMIT 10;
    """

    cursor.execute(query)
    rows = []
    for row in cursor:
        first_name = row[0]
        last_name = row[1]
        rating = row[2]
        salary = row[3]
        rows.append([f"{first_name} {last_name}", rating, f"${salary:.2f}"])

    print(tabulate(rows, headers=["Name", "Rating", "Salary"], tablefmt="fancy_grid"))



