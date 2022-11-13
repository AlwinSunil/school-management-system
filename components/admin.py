from helpers.DBConnect import handleSQLCall, handleSQLType
from helpers.UpdateInfo import UpdateStudentInfo
from colored import fg, bg, attr
from texttable import *
import inquirer

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
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_cols_dtype(["i", "t", "t", "i", "t", "t", "a", "i", "a"])
        table.set_cols_align(["l", "r", "r", "r", "r", "r", "l", "l", "l"])
        tableList = [
            [
                "Adm No",
                "Adm Date",
                "Name",
                "Class",
                "Divison",
                "DOB",
                "Address",
                "Number",
                "Email",
            ]
        ]
        record = handleSQLCall("select * from students;")

        for row in record:
            tableList.append(
                [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
            )
        table.add_rows(tableList)
        print(table.draw())

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

        for row in record:
            color = fg(50)
            att = attr(0)
            for field in range(len(printFields)):
                print(printFields[field], color + str(row[field]) + att)
        print("==================================================")

        UpdateStudentInfo(admn, "students")

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
            print("Raw result from SQL server: ", record)

        print("==================================================")
