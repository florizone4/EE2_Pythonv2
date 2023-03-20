import mysql.connector
from datetime import datetime

# establish a connection to the remote MySQL server
cnx = mysql.connector.connect(user='a22ib2a03', password='secret',
                              host='mysql.studev.groept.be', port='3306', database='a22ib2a03')

# create a cursor object to execute SQL queries
cursor = cnx.cursor()

# define the data to be inserted
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
event = "some event"

# execute the INSERT statement
query = "INSERT INTO PytonLogs (time, event) VALUES (%s, %s)"
values = (time, event)
cursor.execute(query, values)

# commit the transaction
cnx.commit()

# close the cursor and connection
cursor.close()
cnx.close()