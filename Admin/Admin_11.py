import mysql.connector
from datetime import datetime, timedelta

cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()


def add_product(category_id, name, quantity_in_stock, price, discount, storage_type, rating, description, warehouse_ID):

        # Construct the SQL query
    sql = """
        INSERT INTO Product (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (category_id, name, quantity_in_stock, price, discount, storage_type, rating, description)

    # Execute the SQL query
    cursor.execute(sql, values)

    # Commit the changes to the database
    cnx.commit()

    # Get the auto-generated productID
    product_id = cursor.lastrowid
    sql2 = """
    INSERT INTO inventory ( productID, quantity, storage_type, WarehouseID )
    values (%s, %s, %s, %s)"""
    values2=(product_id, quantity_in_stock, storage_type,warehouse_ID)
    cursor.execute(sql2,values2)
    cnx.commit()
    
    print(f"New product '{name}' added with productID {product_id}.")
    return product_id



# Example usage






