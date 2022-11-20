import inquirer
from colored import fg, bg, attr
from components.functions import showAllRecords
from helpers.DBConnect import handleSQLCall
from helpers.DisplayInfo import displayInfoPrint
from helpers.UpdateInfo import updateInfoStudent
from texttable import *

QueryDef = [
    inquirer.List(
        "admin",
        message="Select option :",
        choices=[
            "Show all records",
            "Get specific record",
            "Run custom mySQL commands",
            "Add new Student/ProgressCard/Teacher",
        ],
        default="Get specific record",
    ),
]

UpdateQueryDef = [
    inquirer.List(
        "update",
        message="Do you want to update records??",
        choices=[
            "yes",
            "no",
        ],
        default="no",
    ),
]

AddDataQueryDef = [
    inquirer.List(
        "add",
        message="Whose data your are adding??",
        choices=[
            "Student",
            "ProgressCard",
            "Teacher",
        ],
        default="Student",
    ),
]


def AddNewData(database):
    record = handleSQLCall("desc " + database + ";")
    record = record["data"]

    attributes = list()
    for att in record:
        attributes.append(att[0])

    data = list()
    for att in attributes:
        inputData = input("Enter " + att + " : ")
        if inputData.isnumeric() == True:
            inputData = int(inputData)
        data.append(inputData)
    data = str(tuple(data))

    SQL_QUERY = "INSERT INTO " + database + " VALUES" + data + " ;"
    record = handleSQLCall(SQL_QUERY, option="insert", database=database)


def main():
    print("%s Logged in as Admin %s" % (fg(2), attr(0)))

    res = inquirer.prompt(QueryDef)
    if res["admin"] == "Show all records":
        showAllRecords("students")

    elif res["admin"] == "Get specific record":
        color = fg(13)
        att = attr(0)
        admn = input(color + "Enter admission no : " + att)
        print("==================================================")

        SQL_QUERY = (
            "SELECT S.*, T.name AS class_teacher_name FROM students S, class_teachers T WHERE S.class = T.class AND adm_no = "
            + admn
            + ";"
        )
        record = handleSQLCall(SQL_QUERY)

        printFields = [
            "Admission No: ",
            "Admission Date: ",
            "Name: ",
            "Class: ",
            "Divison: ",
            "Date of birth: ",
            "Address: ",
            "Phone Number: ",
            "Email: ",
            "Class Teacher: ",
        ]

        displayInfoPrint(printFields, record["data"], color_fg=50, color_att=0)

        updateInfoStudent(admn, "students")

    elif res["admin"] == "Run custom mySQL commands":
        print(
            fg(1)
            + "WARNING!! This option gives access to enter any SQL command"
            + attr(0)
        )
        print(fg(15) + bg(1) + "USE UNDER YOUR RISK!!" + attr(0))

        SQL_QUERY = input("Enter the mySQL command or (go back enter, exit) : ")

        if SQL_QUERY != "exit":
            record = handleSQLCall(SQL_QUERY)
            print("Raw result from SQL server: ", record["data"])

        print("==================================================")

    elif res["admin"] == "Add new Student/ProgressCard/Teacher":
        res = inquirer.prompt(AddDataQueryDef)

        if res["add"] == "Student":
            AddNewData("students")

        elif res["add"] == "ProgressCard":
            AddNewData("progresscard")

        elif res["add"] == "Teacher":
            AddNewData("class_teachers")
