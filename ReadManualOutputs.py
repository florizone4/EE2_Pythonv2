import mysql.connector

def read_last_row_from_database():
    # Connect to the database
    #if no connection to the database is possible, automatic mode will continue with the except part
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
        query = "SELECT ID, autoPump, autoLed, autoFan, ManualPump, ManualLed, ManualFan, IsPumpManual, IsLedManual, IsFanManual FROM manualOutputsControl" #ORDER BY ID DESC LIMIT 1"
        cursor.execute(query)

        # Fetch the data from the cursor object
        data = cursor.fetchone()
        print(data)

        # Close the cursor and database connections
        cursor.close()
        cnx.close()

        # Return the data


        return data


    except:
        print("connection not made")
        return []