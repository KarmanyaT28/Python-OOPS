import mysql.connector

# --- Connection Parameters ---
# Ensure these match the configuration of your Dockerized MySQL server:
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "pyuser",
    "password": "pytest",
    "database": "pycharm_db",  # The database created in Step 1
    "charset": "utf8mb4"
}
# -----------------------------

try:
    # 1. Connect to the database
    mydb = mysql.connector.connect(**DB_CONFIG)

    if mydb.is_connected():
        print("✅ CONNECTION SUCCESSFUL!")

        # 2. Get a cursor to execute commands
        mycursor = mydb.cursor()

        # 3. Example: Insert a single record into a table named 'Users'
        #    (Assuming the 'Users' table was created successfully)
        sql = "INSERT INTO Users (username, status) VALUES (%s, %s)"
        val = ("Jane_Developer", "Active")
        mycursor.execute(sql, val)

        # 4. Commit the changes to make the insertion permanent
        mydb.commit()
        print(f"✅ Record inserted successfully. ID: {mycursor.lastrowid}")

except mysql.connector.Error as err:
    print(f"❌ Database Error: {err.msg}")

finally:
    # 5. Close the connection safely
    if 'mydb' in locals() and mydb and mydb.is_connected():
        mydb.close()