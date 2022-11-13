from helpers.DBConnect import handleSQLCall, handleSQLType
import inquirer
from texttable import *

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


def UpdateStudentInfo(admn, database):
    UpdateQueryRes = inquirer.prompt(UpdateQueryDef)

    if UpdateQueryRes["update"] == "yes":
        record = handleSQLCall("desc " + database + ";")

        attributes = list()
        for att in record:
            attributes.append(att[0])

        UpdateAttrQueryDef = [
            inquirer.List(
                "update",
                message="Choose the attribute to update: ",
                choices=attributes,
            ),
        ]

        UpdateAttrQueryRes = inquirer.prompt(UpdateAttrQueryDef)

        for attribute in attributes:
            if UpdateAttrQueryRes["update"] == attribute:
                newData = input("Enter new data for the field, " + attribute + ": ")

                SQL_QUERY = (
                    "update "
                    + database
                    + " set "
                    + attribute
                    + "="
                    + handleSQLType(newData)
                    + " WHERE adm_no="
                    + admn
                    + ";"
                )

                handleSQLCall(SQL_QUERY, attribute)
