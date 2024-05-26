import mysql.connector

try:
    cnx = mysql.connector.connect(
        user='hbnb_dev',
        password='',
        host='localhost',
        database='hbnb_dev_db'
    )
    print("Connected to MySQL!")
    cnx.close()
except mysql.connector.Error as err:
    print("Error: {}".format(err))

