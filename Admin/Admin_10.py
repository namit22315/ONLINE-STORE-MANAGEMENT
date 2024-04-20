import mysql.connector
from datetime import datetime, timedelta

cnx = mysql.connector.connect(user='root', password='Namit@123', host='localhost', port='3306',
                              database='online retail store')
cursor = cnx.cursor()


def assign_delivery_partner(order_id):
    check_order_query = """
    SELECT orderID, status
    FROM `Order` WHERE orderID = %s
    """
    cursor.execute(check_order_query, (order_id,))
    order_info = cursor.fetchone()

    if not order_info:
        print(f"Order {order_id} not found.")
        return
    elif order_info[1] != "Processing":
        print(f"Order {order_id} is already assigned or not in 'Processing' state.")
        return

    # Proceed since order is in 'Processing' state and not yet assigned
    # Get the customer details for the order
    get_customer_query = """
        SELECT c.house_number, c.street_name, c.city, c.pincode
        FROM `Order` o
        JOIN Customer c ON o.username = c.username
        WHERE o.orderID = %s
    """
    cursor.execute(get_customer_query, (order_id,))

    customer_details = cursor.fetchone()

    if customer_details:
        delivery_house_number, delivery_street_name, delivery_city, delivery_pincode = customer_details

        # Find the closest available delivery partner
        find_partner_query = """
            SELECT deliveryID, pickup_house_number, pickup_street_name, pickup_city, pickup_pincode
            FROM DeliveryPartner
            WHERE status = 'Free'
            ORDER BY SQRT(
                POW(SUBSTRING(pickup_pincode, 1, 3) - SUBSTRING(%s, 1, 3), 2) +
                POW(SUBSTRING(pickup_pincode, 4, 3) - SUBSTRING(%s, 4, 3), 2)
            )
            LIMIT 1
        """
        cursor.execute(find_partner_query, (delivery_pincode, delivery_pincode))
        partner_details = cursor.fetchone()

        if partner_details:
            delivery_id, _ = partner_details[:2]  # Using only delivery_id; ignoring address components

            # Update the delivery partner details, status, and expected arrival
            expected_arrival = datetime.now() + timedelta(minutes=120)  # Updated to 120 minutes
            update_partner_query = """
                UPDATE DeliveryPartner
                SET status = 'Occupied',
                    orderID = %s,
                    delivery_house_number = %s,
                    delivery_street_name = %s,
                    delivery_city = %s,
                    delivery_pincode = %s,
                    expected_arrival_time = %s
                WHERE deliveryID = %s
            """
            update_values = (
                order_id, delivery_house_number, delivery_street_name, delivery_city, delivery_pincode,
                expected_arrival,
                delivery_id)
            cursor.execute(update_partner_query, update_values)
            update_order_status_query = """
                UPDATE `Order`
                SET status = 'Shipped'
                WHERE orderID = %s
            """
            cursor.execute(update_order_status_query, (order_id,))

            cnx.commit()

            print(f"Delivery partner {delivery_id} assigned to order {order_id}. Order status updated to 'Shipped'.")
        else:
            print("No available delivery partners found.")
    else:
        print(f"Order {order_id} not found.")
