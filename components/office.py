from colored import fg, attr
from helpers.DBConnect import handleSQLCall
import inquirer
from texttable import *
from helpers.UpdateInfo import UpdateStudentInfo

QueryDef = [
    inquirer.List(
        "read",
        message="Select option :",
        choices=[
            "Get details of student",
            "Get Fee details of student",
            "Show records of all students",
        ],
        default="Get details of student",
    ),
]


def main():
    print("%s Logged in as Office %s" % (fg(2), attr(0)))
    res = inquirer.prompt(QueryDef)

    if res["read"] == "Show records of all students":
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

    elif res["read"] == "Get details of student":
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

    elif res["read"] == "Get Fee details of student":
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

        def getStatus(data):
            if data == 1:
                return "Paid"
            elif data == 0:
                return "Not Paid"
            else:
                return data

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

        for row in record:
            for field in range(len(printFields)):
                print(printFields[field], color + str(getStatus(row[field])) + att)

        record = UpdateStudentInfo(admn, "feepayment")
        print(record)
