from colored import fg, attr


def getStatus(data):
    if data == 1:
        return "Paid"
    elif data == 0:
        return "Not Paid"
    else:
        return data


def displayInfoPrint(printFields, record, color_fg, color_att):
    color_fg = fg(50)
    color_att = attr(0)
    for row in record:
        for field in range(len(printFields)):
            print(printFields[field], color_fg + str(getStatus(row[field])) + color_att)
    print("==================================================")
