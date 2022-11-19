import inquirer
from colored import fg, bg, attr
from components.functions import showAllRecords
from helpers.DBConnect import handleSQLCall
from helpers.DisplayInfo import displayInfoPrint
from helpers.UpdateInfo import updateInfoStudent
from texttable import *

QueryDef = [
    inquirer.List(
        "read",
        message="Select option :",
        choices=[
            "Show all records",
            "Get specific record",
            "Run custom mySQL commands",
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


def main():
    print("%s Logged in as Admin %s" % (fg(2), attr(0)))


def read():
    res = inquirer.prompt(QueryDef)
    if res["read"] == "Show all records":
        showAllRecords("students")

    elif res["read"] == "Get specific record":
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

    elif res["read"] == "Run custom mySQL commands":
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
