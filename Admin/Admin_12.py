import mysql.connector
from datetime import datetime, timedelta

cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()


def remove_product(product_id):

    # Construct the SQL query
    sql3 = "DELETE FROM cart WHERE productID = %s"
    values = (product_id,)
    cursor.execute(sql3, values)
    sql2 = "Delete FROM inventory WHERE productID = %s"
    values2 = (product_id,)
    cursor.execute(sql2,values2)
    cnx.commit()
    # Commit the changes to the database
    cnx.commit()
    sql = "DELETE FROM Product WHERE productID = %s"
    values = (product_id,)

    # Execute the SQL query
    cursor.execute(sql, values)

    # Commit the changes to the database
    cnx.commit()

    # Check if any rows were affected







