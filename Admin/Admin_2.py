import mysql.connector
from datetime import datetime, timedelta
from tabulate import tabulate

cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()

def get_curated_sales_data():
    # Get the current quarter
    today = datetime.now()
    quarter = (today.month - 1) // 3 + 1

    # Calculate the start and end dates of the current quarter
    year = today.year
    quarter_start = datetime(year, (quarter - 1) * 3 + 1, 1)
    quarter_end = quarter_start + timedelta(days=92)

    # Query to get the curated sales data for each category
    query = """
        SELECT c.category_name,
               c.category_discount,
               SUM(p.price * ca.quantity * (1 - p.discount / 100)) AS total_sales,
               SUM(p.price * ca.quantity * (1 - p.discount / 100) * (1 - c.category_discount / 100)) AS discounted_sales,
               COUNT(DISTINCT o.orderID) AS order_count
        FROM Cart ca
        JOIN Product p ON ca.productID = p.productID
        JOIN Category c ON p.categoryID = c.categoryID
        JOIN `Order` o ON o.username = ca.username
        WHERE o.date_order_placed BETWEEN %s AND %s
        GROUP BY c.category_name, c.category_discount
    """
    values = (quarter_start, quarter_end)
    cursor.execute(query, values)
    results = cursor.fetchall()

    headers = ["Category", "Discount (%)", "Total Sales", "Discounted Sales", "Order Count"]
    rows = []
    for row in results:
        category_name, category_discount, total_sales, discounted_sales, order_count = row
        rows.append([category_name, category_discount, total_sales, discounted_sales, order_count])

    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))