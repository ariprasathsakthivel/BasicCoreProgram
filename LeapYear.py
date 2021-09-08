'''
@Author: Ariprasath
@Date: 2021-09-08 08:35:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 08:46:00
@Title : Leap year validator
'''

def leap_year_check(year):
    '''
    Args:
        year: Year in the format YYYY
    Action:
        Validates the year is leap year or not
    Return:
        A string representing leap year or not
    Raises:
        None
     '''
    if year%400 == 0 or (year%100 != 0 and year%4 == 0):
        print("{} is a leap year".format(year))
    else:
        print("{} is a non-leap year".format(year))


def leap_year():
    '''
    Args:
        None
    Action:
        Gets the year from the user and validates whether it is in the format YYYY
    Returns:
        None
    Raises:
        None        
    '''
    year=input("Enter the year in the format YYYY\n")
    if len(year)!=4:
        print("You have entered the year in a wrong format\n")
        leap_year()
    else:
        leap_year_check(int(year))

if __name__=="__main__":
    leap_year()