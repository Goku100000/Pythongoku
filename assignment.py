year = int(input("Enter year:"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "Is not a leap year")
2005