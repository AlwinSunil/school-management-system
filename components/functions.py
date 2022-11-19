from colored import fg, attr
from helpers.DBConnect import handleSQLCall
from helpers.DisplayInfo import displayInfoPrint
from helpers.UpdateInfo import updateInfoStudent
from texttable import *


def showAllRecords(sqlTable):
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
    record = handleSQLCall("select * from " + sqlTable + ";")
    record = record["data"]
    for row in record:
        tableList.append(
            [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
        )
        table.add_rows(tableList)
        print(table.draw())


def showStudentRecords():
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
