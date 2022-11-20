import inquirer
from colored import fg, attr
from components.functions import showAllRecords
from helpers.DBConnect import handleSQLCall
from helpers.DisplayInfo import displayInfoPrint
from helpers.UpdateInfo import updateInfoStudent
from texttable import *

QueryDef = [
    inquirer.List(
        "office",
        message="Select option :",
        choices=[
            "Get details of student",
            "Check/Update FEE details of student",
            "Show records of all students",
        ],
        default="Get details of student",
    ),
]


def main():
    print("%s Logged in as Office %s" % (fg(2), attr(0)))
    res = inquirer.prompt(QueryDef)

    if res["office"] == "Show records of all students":
        showAllRecords("students")

    elif res["office"] == "Get details of student":
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

    elif res["office"] == "Check/Update FEE details of student":
        color = fg(50)
        att = attr(0)
        admn = input(color + "Enter admission no : " + att)
        print("==================================================")
        SQL_QUERY = (
            "SELECT S.adm_no, S.name, S.class, F.term_1, F.term_2, F.term_3, FP.term_1, FP.term_1_payment_date, FP.term_2, FP.term_2_payment_date, FP.term_3, FP.term_3_payment_date FROM students S, fees F, feepayment FP WHERE S.class = F.class AND S.adm_no = "
            + admn
            + ";"
        )
        record = handleSQLCall(SQL_QUERY)

        printFields = [
            "Adm No: ",
            "Name:",
            "Class: ",
            "Fees: 1st Term: ",
            "Fees: 2nd Term: ",
            "Fees: 3rd Term: ",
            "1st Term Status: ",
            "1st Term Payment Date: ",
            "2nd Term Status: ",
            "2nd Term Payment Date: ",
            "3rd Term Status: ",
            "3rd Term Payment Date: ",
        ]
        displayInfoPrint(printFields, record["data"], color_fg=50, color_att=0)

        record = updateInfoStudent(admn, "feepayment")
