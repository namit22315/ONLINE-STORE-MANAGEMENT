import mysql.connector

from tabulate import tabulate
import mysql.connector
from datetime import datetime, timedelta

cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()


def view_and_update_inventory():
    # Query to fetch products
    query = """
    SELECT p.productID, p.name, p.quantity_in_stock, i.quantity, i.storage_type, w.Manager, w.phone_number
    FROM Product p
    JOIN Inventory i ON p.productID = i.productID
    JOIN Warehouse w ON i.WarehouseID = w.WarehouseID
    ORDER BY p.productID;
    """

    cursor.execute(query)

    # Prepare data for tabulate
    table_data = []
    for row in cursor:
        product_id = row[0]
        product_name = row[1]
        stock_quantity = row[2]
        inventory_quantity = row[3]
        storage_type = row[4]
        manager_name = row[5]
        phone_number = row[6]
        table_data.append(
            [product_id, product_name[:15], stock_quantity, inventory_quantity, storage_type, manager_name,
             phone_number])

    # Print the results in a fancy grid format
    headers = ["ID", "Name", "Stock", "Inventory", "Storage", "Warehouse Manager", "Phone Number"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    # Prompt for product ID and new quantity
    product_id = int(input("\nEnter the product ID to update inventory: "))
    new_quantity = int(input("Enter the new quantity: "))

    # Update the inventory quantity
    try:
        update_query = """
        UPDATE Inventory i
        JOIN Product p ON i.productID = p.productID
        SET i.quantity = %s, p.quantity_in_stock = %s
        WHERE i.productID = %s;
        """
        values = (new_quantity, new_quantity, product_id)
        cursor.execute(update_query, values)
        cnx.commit()
        print(f"Inventory updated successfully for product ID {product_id}.")
    except Exception as e:
        print(f"Error updating inventory: {e}")
        cnx.rollback()




