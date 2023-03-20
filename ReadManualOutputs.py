import mysql.connector

def read_last_row_from_database():
    # Connect to the database
    try:
        cnx = mysql.connector.connect(
            host="mysql.studev.groept.be",
            user="a22ib2a03",
            password="secret",
            database="a22ib2a03"
        )
        # Create a cursor object
        cursor = cnx.cursor()

        # Execute the SELECT statement to retrieve the last row from the table
        query = "SELECT id, pump, led, fan, boolean FROM my_table ORDER BY id DESC LIMIT 1"
        cursor.execute(query)

        # Fetch the data from the cursor object
        data = cursor.fetchone()

        # Close the cursor and database connections
        cursor.close()
        cnx.close()

        # Return the data
        if (data[4] == 1): #if manual mode ON

            return data
        else:
            return []

    except:
        return []