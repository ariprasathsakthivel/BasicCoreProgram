'''
@Author: Ariprasath
@Date: 2021-09-08 18:55:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 19:24:00
@Title : Prime factors
'''
num=int(input("Enter a number to find the prime factors"))
while num % 2 == 0:
    print (2)
    num = num / 2

for i in range(3,int(num),2):
    
    while (num % i == 0):
        print (i)
        num = num / i