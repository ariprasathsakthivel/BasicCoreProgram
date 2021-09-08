'''
@Author: Ariprasath
@Date: 2021-09-08 18:43:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 18:50:00
@Title : Harmonic number
'''

limit=int(input("Enter the limit\n"))
initial_value=1
while initial_value<=limit:
    if initial_value<limit:
        print(f"1/{initial_value}+",end='')
    elif initial_value==limit:
        print(f"1/{initial_value}",end='')
    initial_value+=1    