def is_leap(year):
    leap = False

    # leap year check
    # year % 400 == 0
    # year % 100 != 0 and year % 4 == 0

    if (year % 400 == 0):
        leap = True
    elif (year % 100 == 0):
        leap = False
    elif (year % 4 == 0):
        leap = True

    return leap


year = int(input("Type the year : "))
print(is_leap(year))
