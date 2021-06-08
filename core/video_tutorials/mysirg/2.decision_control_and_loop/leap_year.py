def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))


year = int(input("Enter the year: "))
print("Year is {}.".format(year))
leap_year(year)
