from colored import fg, attr
import inquirer
from components.functions import showStudentRecords
from helpers.DBConnect import handleSQLCall
from helpers.DisplayInfo import displayInfoPrint
from helpers.UpdateInfo import updateInfoStudent

QueryDef = [
    inquirer.List(
        "teacher",
        message="Select option :",
        choices=[
            "Get details of student",
            "See progress card of student",
        ],
        default="Get details of student",
    ),
]


def main():
    print("%s Logged in as Teacher %s" % (fg(2), attr(0)))
    res = inquirer.prompt(QueryDef)

    if res["teacher"] == "See progress card of student":
        color = fg(13)
        att = attr(0)
        admn = input(color + "Enter admission no : " + att)
        print("==================================================")
        SQL_QUERY = (
            "SELECT S.name, S.class, S.division, T.name AS class_teacher_name, P.* FROM students S, class_teachers T, progresscard P WHERE S.class = T.class AND P.adm_no = S.adm_no AND S.adm_no="
            + admn
            + ";"
        )
        record = handleSQLCall(SQL_QUERY)

        printFields = list()
        for col in record["columns"]:
            printFields.append(col.capitalize().replace("_", " ") + ": ")

        print("Progress Report of ")
        displayInfoPrint(printFields, record["data"], color_fg=50, color_att=0)

        updateInfoStudent(admn, "progresscard")

    elif res["teacher"] == "Get details of student":
        showStudentRecords()
