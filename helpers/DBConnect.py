from mysql.connector import Error
from colored import fg, attr
import mysql.connector

print("==================================================")
print("%s Initializing connection to mySQL server %s" % (fg(4), attr(0)))

try:
    connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="9846")
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print(fg(2)+" Connected to MySQL Server version " + db_Info + attr(0))
        cursor = connection.cursor()
        cursor.execute("use school;")
        # here record type is list
        print(" You're connected to database: school")

except Error as e:
    print(fg(1) + " Error while connecting to MySQL : " + e + attr(0))

#     code to close connection
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

print("==================================================")
