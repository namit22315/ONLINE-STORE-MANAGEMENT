import mysql.connector
from datetime import datetime, timedelta
cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()

# Create a cursor object



def add_category():
    new_category_name = input("Enter category name: ")
    new_category_discount = int(input("Enter category discount: "))
    """
    Add a new category to the Category table.

    Args:
        category_name (str): The name of the new category.
        category_discount (float): The discount percentage for the new category.

    Returns:
        int: The auto-generated categoryID of the new category, or None if an error occurred.
    """
    try:
        # Construct the SQL query
        sql = "INSERT INTO Category (category_name, category_discount) VALUES (%s, %s)"
        values = (new_category_name, new_category_discount)

        # Execute the SQL query
        cursor.execute(sql, values)

        # Commit the changes to the database
        cnx.commit()

        # Get the auto-generated categoryID
        category_id = cursor.lastrowid
        print(f"New category '{new_category_name}' added with categoryID {category_id}.")

    except Exception as e:
        # Roll back the changes in case of an error
        cnx.rollback()
        print(f"Error adding category: {e}")



# Example usage


# if new_category_id:
#     print(f"New category '{new_category_name}' added with categoryID {new_category_id}.")
# else:
#     print("Failed to add new category.")

# Close the database connection
