import inquirer

LoginQueryDef = [
    inquirer.List(
        "login",
        message="Choose your section : ",
        choices=["For Admin", "For Office", "For Teachers"],
        default="For Teachers",
    ),
]

ExitQueryDef = [
    inquirer.List(
        "exit",
        message="Do you wanna exit the app?(y/n)",
        choices=["yes", "no"],
        default="no",
    ),
]
