'''
@Author: Ariprasath
@Date: 2021-09-08 08:35:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 08:46:00
@Title : Leap year validator
'''

def leap_year_check(year):
    if year%400 == 0:
        print("{} is a leap year".format(year))
    elif year%100 == 0:
        print("{} is a non-leap year".format(year))
    elif year%4 == 0:
        print("{} is a leap year".format(year))
    else:
        print("{} is a non-leap year".format(year))


def leap_year():
    year=input("Enter the year in the format YYYY\n")
    if len(year)!=4:
        print("You have entered the year in a wrong format\n")
        leap_year()
    else:
        leap_year_check(int(year))

leap_year()
