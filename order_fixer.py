import mysql.connector
import schedule
import time
import mysql.connector
from datetime import datetime, timedelta
from tabulate import tabulate



def clean_orders():
    cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                                  database='online retail store')
    cursor = cnx.cursor()
    select_query = """
            SELECT * FROM `online retail store`.`order`
            WHERE orderID NOT IN (SELECT orderID FROM billing);
            """

    # Execute the select query
    cursor.execute(select_query)
    records = cursor.fetchall()

    # Print the records that will be deleted
    if records:
        print(f"Records to be deleted at {time.strftime('%Y-%m-%d %H:%M:%S')}:")
        for record in records:
            print(record)

        # SQL command to delete orders without corresponding billing records
        delete_query = """
                DELETE FROM `online retail store`.`order`
                WHERE orderID NOT IN (SELECT orderID FROM billing);
                """
        cursor.execute(delete_query)
        cnx.commit()
        print(f"Deleted {cursor.rowcount} records.")

    else:
        print(f"No records to delete at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    cursor.close()




def job():
    print("Running clean up job...")
    clean_orders()




def scheduled_job_1():

    # Schedule the job to run daily at midnight
    schedule.every(10).seconds.do(job)

    # Keep the script running in a loop
    while True:
        schedule.run_pending()
        time.sleep(1)
