'''
@Author: Ariprasath
@Date: 2021-09-08 07:46:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 08:02:00
@Title : Print a string
'''

def string_display():
    user_name=input("Enter you name which has minimum 3 letters\n")
    if len(user_name)<3:
        print("The name entered by you contains less than 3 letters")
        string_display()
    else:
        return user_name


print("Hello {}, How are you?".format(string_display()))
