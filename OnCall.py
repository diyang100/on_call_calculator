def onCall(year, month, date):
    base = [2019, 12, 30]
    daysAway = 0

    while (year != base[0]):
        if (year > base[0]):
            if ((base[0] + 1) % 4 == 0):
                daysAway += 366
            else:
                daysAway += 365

            base = [(base[0] + 1), base[1], base[2]]
        else:
            if (base[0] % 4 == 0):
                daysAway -= 366
            else:
                daysAway -= 365

            base = [(base[0] - 1), base[1], base[2]]

    while (month != base[1]):
        if (base[1] > 8):
            if (base[1] % 2 == 1):
                daysAway -= 31
            else:
                daysAway -= 30

            base = [base[0], (base[1] - 1), base[2]]
        else:
            if (base[1] - 1 == 2 and base[0] % 4 == 0):
                daysAway -= 29
            elif (base[1] - 1 == 2):
                daysAway -= 28
            elif (base[1] % 2 == 1):
                daysAway -= 30
            else:
                daysAway -= 31
            base = [base[0], (base[1] - 1), base[2]]
    daysAway = daysAway + (date - base[2])
    print("The date is " + str(abs(daysAway)) + " days away from the base")
    if (daysAway >= 0):
        weeksAway = daysAway // 7
        if (weeksAway % 4 == 0):
            return True
        else:
            return False
    else:
        weeksAway = (abs(daysAway) + 6) // 7
        if (weeksAway % 4 == 0):
            return True
        else:
            return False

def onCallMain():
    print("Enter a date (yyyy mm dd): \n")
    dateList = input().split()
    if onCall(int(dateList[0]), int(dateList[1]), int(dateList[2])):
        print("The date is an on-call date.")
    else:
        print("The date is not an on-call date.")

onCallMain()