# Leap Year

year = int(input("Enter the YEAR: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, ": is a LEAP YEAR")
        else:
            print(year, ": is NOT a LEAP YEAR")
    else:
        print(year, ": is a LEAP YEAR")
else:
    print(year, ": is NOT a LEAP YEAR")

    