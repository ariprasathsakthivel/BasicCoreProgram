'''
@Author: Ariprasath
@Date: 2021-09-08 19:46:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 20:38:00
@Title : find three numbers from a array that adds to zero
'''

import random

def zero_check(integers):
    '''
    Description:
        Finds the three distinct integers that sums to zero
    Parameter: 
        integers(list): A list containing integers  between -9 and 9
    Return:
        Three distinc intgers
    '''
    for i in range(0,len(integers)):
        for j in range(i+1,len(integers)):
            for k in range(j+1,len(integers)):
                sum=integers[i]+integers[j]+integers[k]
                if sum==0:
                    print(f"{integers[i]},{integers[j]},{integers[k]}")

if __name__=="__main__":
    integers=[]
    sum=0
    for i in range(0,10):
        integers.append(random.randint(-9,9))
    zero_check(integers)