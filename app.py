import inquirer
from helpers import DBConnect
from colored import fg, bg, attr
from components import admin, office, teacher
from QueryList import LoginQueryDef, ExitQueryDef

app = True
USERACCESS = None

while app == True:
    color = fg(13)
    att = attr(0)
    print('%s School management system %s' % (fg(3), attr(0)))
    LoginQuery = inquirer.prompt(LoginQueryDef)

    if LoginQuery["login"] == "For Admin":
        if USERACCESS == None:
            pwd = input(color + "Enter password to enter: " + att)
            if (pwd == "123"):
                admin.main()
                USERACCESS = "admin"

    if LoginQuery["login"] == "For Office":
        office.main()

    if LoginQuery["login"] == "For Teachers":
        teacher.main()

    if USERACCESS == "admin":
        admin.read()

    ExitQuery = inquirer.prompt(ExitQueryDef)

    if ExitQuery["exit"] == "yes":
        app = False
        USERACCESS = None
        print("App closed")
    else:
        app = True
        USERACCESS = USERACCESS
