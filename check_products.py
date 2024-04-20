import mysql.connector
import schedule
import time


def check_product_inventory():
    connection = None
    try:
        # Connect to your MySQL database
        connection = mysql.connector.connect(
            user='root',
            password='Namit@123',
            host='localhost',
            database='online retail store'
        )
        cursor = connection.cursor()

        # SQL command to find products that are not in inventory but should be
        find_faulty_query = """
            SELECT p.productID, p.name
            FROM Product p
            LEFT JOIN Inventory i ON p.productID = i.productID
            WHERE p.quantity_in_stock > 0 AND i.productID IS NULL;
            """

        # Execute the query to find faulty products
        cursor.execute(find_faulty_query)
        faulty_products = cursor.fetchall()

        # Check if there are any faulty products found
        if faulty_products:
            print(f"Faulty products found at {time.strftime('%Y-%m-%d %H:%M:%S')}:")
            for productID, name in faulty_products:
                print(f"Product ID: {productID}, Name: {name}")

            faulty_product_ids = [str(productID) for productID, _ in faulty_products]
            delete_query = f"DELETE FROM Product WHERE productID IN ({','.join(faulty_product_ids)})"
            cursor.execute(delete_query)
            connection.commit()
            print(f"Deleted {cursor.rowcount} faulty products from the database.")

        else:
            print(f"No faulty products to delete at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()


def job():
    print("Running inventory check...")
    check_product_inventory()


def scheduled_job():
    # Schedule the job to run every 10 minutes
    schedule.every(10).seconds.do(job)

    # Keep the script running in a loop
    while True:
        schedule.run_pending()
        time.sleep(1)



