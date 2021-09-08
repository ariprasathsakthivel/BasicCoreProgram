'''
@Author: Ariprasath
@Date: 2021-09-08 18:19:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 18:36:00
@Title : Powers of 2
'''
import math

count=int(input("Enter the limit"))
initial_value=0
while initial_value!=count:
    print(int(math.pow(2,initial_value)))
    initial_value+=1
