import datetime
import random
import time
import readSMS
import mysql.connector
def pushtoDB(LDR, AHS, SMS, NTC):


    database = mysql.connector.connect(
        host="mysql.studev.groept.be",
        user="a22ib2a03",
        password="secret",
        database="a22ib2a03"
    )

    mycursor = database.cursor(buffered=True)

# ntcArray = []

# readSMS()

    # temperatureVal = random.uniform(20, 30)
    # humidityVal = random.randon()
    # moistVal = random.randon()
    # lightVal = random.random()
    # getId = "SELECT COUNT(ID) FROM measurements"
    # print(rows)
    # mycursor.execute(getId)
    # newRowId = int(mycursor.fetchall()[0][0]) + 1

    # print(newRowId)
    # currentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # currentDateDate = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S")
    # print(currentDateDate)

    # ntcArray.append(temperatureVal)
    # print("temperature registered: [" + str(temperatureVal) + "]")
    # time.sleep(5)

    # insert = "INSERT INTO a22ib2a03.measurements (ID,temperature, time) VALUES (('%s', '%s','%s'),(" + str(newRowId) +","+ str(temperatureVal) +" , " + str(currentDateDate) +"))"  # str(currentDate)
    insert = "INSERT INTO a22ib2a03.measurements (temperature, humidity, moisture,light, time) VALUES ( " + str(NTC) +", "+ str(AHS) +", " + str(SMS) +"," + str(LDR) + " , CURRENT_TIMESTAMP)"
    mycursor.execute(insert)

    # Example query
    mycursor.execute("SELECT * FROM measurements")
    database.commit()

    # Fetch the results
    # myresult = mycursor.fetchall()

    # close the cursor and connection
    mycursor.close()
    database.close()

    # Print the results
    # for row in myresult:
    #     print(row)


