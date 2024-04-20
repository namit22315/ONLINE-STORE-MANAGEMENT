import mysql.connector
from datetime import datetime, timedelta
cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()

def get_inventory_items():

    query = """
        SELECT i.storage_type, GROUP_CONCAT(CONCAT(p.name, ' (', i.quantity, ')') SEPARATOR ', ') AS items
        FROM Inventory i
        JOIN Product p ON i.productID = p.productID
        GROUP BY storage_type;
    """
    cursor.execute(query)

    # Fetch all the rows
    result = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()

    return result