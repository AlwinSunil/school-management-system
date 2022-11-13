from colored import fg, attr
from helpers.DBConnect import handleSQLCall
import inquirer
from texttable import *


QueryDef = [
    inquirer.List(
        "read",
        message="Select option :",
        choices=["Update fee payment", "Show all records", "Get specific record"],
        default="Get specific record",
    ),
]


def main():
    print("%s Logged in as Office %s" % (fg(2), attr(0)))
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
        SQL_CALL = (
            "SELECT S.*, T.name AS class_teacher_name FROM students S, class_teachers T WHERE S.class = T.class AND adm_no = "
            + admn
            + ";"
        )
        record = handleSQLCall(SQL_CALL)

        for row in record:
            color = fg(50)
            att = attr(0)
            print("Admission No: ", end=" ")
            print(color + str(row[0]) + att)
            print("Admission Date: " + color + str(row[1]) + att)
            print("Name: " + color + row[2] + att)
            print("Class: " + color + str(row[3]) + att)
            print("Divison: " + color + row[4] + att)
            print("Date of birth: " + color + str(row[5]) + att)
            print("Address: ", color + row[6] + att)
            print("Phone Number: ", color + row[7] + att)
            print("Email: ", color + row[8] + att)
            print("Class Teacher: ", color + row[9] + att)
        print("==================================================")

    elif res["read"] == "Update fee payment":
        color = fg(50)
        att = attr(0)
        admn = input(color + "Enter admission no : " + att)
        print("==================================================")
        SQL_CALL = (
            "SELECT S.adm_no, S.name, S.class, F.term_1, F.term_2, F.term_3, FP.term_1, FP.term_1_payment_date, FP.term_2, FP.term_2_payment_date, FP.term_3, FP.term_3_payment_date FROM students S, fees F, feepayment FP WHERE S.class = F.class AND S.adm_no = "
            + admn
            + ";"
        )
        record = handleSQLCall(SQL_CALL)

        def getStatus(bool):
            if bool == 1:
                return "Paid"
            elif bool == 0:
                return "Not Paid"

        for row in record:
            print("Adm No: ", color + str(row[0]) + att)
            print("Name:", color + str(row[1]) + att)
            print("Class: ", color + str(row[2]) + att)
            print("Fees: 1st Term: ", color + str(row[3]) + att)
            print("Fees: 2nd Term: ", color + str(row[4]) + att)
            print("Fees: 3rd Term: ", color + str(row[5]) + att)
            print("1st Term Status: ", color + str(getStatus(row[6])) + att)
            print("1st Term Payment Date: ", color + str(row[7]) + att)
            print("2nd Term Status: ", color + str(getStatus(row[8])) + att)
            print("2nd Term Payment Date: ", color + str(row[9]) + att)
            print("3rd Term Status: ", color + str(getStatus(row[10])) + att)
            print("3rd Term Payment Date: ", color + str(row[11]) + att)
