from colored import fg, attr
import mysql.connector
from mysql.connector import Error

print("==================================================")
print("%s Initializing connection to mySQL server %s" % (fg(4), attr(0)))

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="9846")
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print(fg(2) + " Connected to MySQL Server version " + db_Info + attr(0))
        cursor = connection.cursor()
        cursor.execute("use school;")
        print(" You're connected to database: school")

except Error as e:
    print(fg(1) + " Error while connecting to MySQL : " + e + attr(0))

print("==================================================")


def handleSQLCall(query, option=None, database=None, column=None):
    try:
        cursor.execute(query)
        record = cursor.fetchall()
        columns = cursor.column_names
        connection.commit()
        if option == "update":
            print(fg(2) + "Updated " + column + " successfully" + attr(0))
        elif option == "insert":
            print(
                fg(2)
                + "Inserted data into database: "
                + database
                + ", successfully"
                + attr(0)
            )
        return {"columns": columns, "data": record}
    except Error as err:
        print(fg(1) + f"Error: '{err}'" + attr(0))


def handleSQLType(data):
    if data.isnumeric == True:
        instance = int(data)
        return instance
    elif isinstance(data, str) == True:
        return "'" + data + "'"
    else:
        return data
