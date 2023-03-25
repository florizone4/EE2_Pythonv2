import mysql.connector
import requests
import json

def readTable():
    # Connect to the database
    # if no connection to the database is possible, automatic mode will continue with the except part
    try:
        import requests
        response = requests.get("https://studev.groept.be/api/a22ib2a03/returnAutoControls")
        print("Response: ", response)
        parsed = response.json()
        print(parsed)


        # Return the data
        return parsed


    except:

        print("conenction to automatic DBnot made")
        return []




