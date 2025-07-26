# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    """Connects to MySQL server and creates the 'alx_book_store' database if it doesn't exist."""
    connection = None
    try:
        # Establish the connection to MySQL server
        # Replace 'your_username' and 'your_password' with your actual MySQL credentials
        # The host is usually 'localhost' if MySQL is on the same machine
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Your MySQL username, likely 'root' based on prior interactions
            password='WhwIly?Yacbtm.# MySQLServer.py

import mysql.connector
from mysql.connector import Error # <--- THIS LINE IS CRUCIAL FOR 'Error' TO BE DEFINED

def create_database():
    """Connects to MySQL server and creates the 'alx_book_store' database if it doesn't exist."""
    connection = None
    try:
        # Establish the connection to MySQL server
        # Replace 'root' and 'your_password' with your actual MySQL credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password' # <--- IMPORTANT: Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL command to create database if it doesn't exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)

            print("Database 'alx_book_store' created successfully or already exists.")

    except Error as e: # <--- 'Error' is now correctly defined because of the import above
        # Handle connection and other MySQL-related errors
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        # Close the connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()' # <--- IMPORTANT: Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL command to create database if it doesn't exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)

            # Print success message. 'IF NOT EXISTS' handles existing DBs without error.
            print("Database 'alx_book_store' created successfully or already exists.")

    except Error as e:
        # Handle connection and other MySQL-related errors
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        # Close the connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
