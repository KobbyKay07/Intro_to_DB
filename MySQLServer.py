import os
import mysql.connector

try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        auth_plugin='mysql_native_password'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created  successfully!")

except mysql.connector.Error as e:
    print(f"Database Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
