import csv
from colored import fg, bg, attr
from texttable import *
import inquirer

QueryDef = [
    inquirer.List("read", message="Select option :",
                  choices=["Show all records", "Get specific record"], default="Get specific record"),
]


def main():
    print("%s Logged in as Admin %s" % (fg(2), attr(0)))


def read():
    with open("admin.csv") as csvFile:
        res = inquirer.prompt(QueryDef)
        readDB = csv.reader(csvFile, delimiter=',')
        if (res['read'] == "Show all records"):
            table = Texttable()
            table.set_deco(Texttable.HEADER)
            table.set_cols_dtype(['i', 't', 'i', 't',  'a', 'i', 'a'])
            table.set_cols_align(["l", "r", "r", "r", "l", "l", "l"])
            tableList = [["Adm No", "Name", "Class",
                          "Divison", "Address", "Number", "Email"]]
            for row in readDB:
                tableList.append(
                    [row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
            table.add_rows(tableList)
            print(table.draw())
        elif (res['read'] == "Get specific record"):
            color = fg(13)
            att = attr(0)
            admn = input(color + "Enter admission no : " + att)
            print("==================================================")
            for row in readDB:
                if row[0] == admn:
                    color = fg(50)
                    att = attr(0)
                    print("Admission No:", end=" ")
                    print(color + row[0] + att)
                    print("Name:" + color + row[1] + att)
                    print("Class:" + color + row[2] + att)
                    print("Divison:" + color + row[3] + att)
                    print("Address:", color + row[4] + att)
                    print("Number:", color + row[5] + att)
                    print("Email:", color + row[6] + att)
            print("==================================================")
