import datetime
import random
import time

import mysql.connector

database = mysql.connector.connect(
    host="mysql.studev.groept.be",
    user="a22ib2a03",
    password="secret",
    database="a22ib2a03"
)

mycursor = database.cursor(buffered=True)

while True:
    temperatureVal = random.uniform(20, 30)
    getId = "SELECT COUNT(ID) FROM measurements"
    #print(rows)
    mycursor.execute(getId)
    newRowId = int(mycursor.fetchall()[0][0]) + 1

    print(newRowId)
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    currentDateDate = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S")
    print(currentDateDate)

    ntcArray.append(temperatureVal)
    print("temperature registered: [" + str(temperatureVal) + "]")
    time.sleep(5)

    # Example query
    mycursor.execute("SELECT * FROM measurements")
    database.commit()

    # Fetch the results
    myresult = mycursor.fetchall()

    # Print the results
    for row in myresult:
        print(row)


