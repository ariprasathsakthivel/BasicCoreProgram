'''
@Author: Ariprasath
@Date: 2021-09-08 08:15:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 08:30:00
@Title : Flip coin and print percentage of head and tail
'''

import random

if __name__=="__main__":
    count=abs(int(input("How many times do you want to flip the coin\n")))

    percent_count=count
    head_count=0
    tail_count=0
    while count>0:
        num=random.randint(0,1)
        count-=1
        if num==0:
            head_count+=1
        else:
            tail_count+=1

print("Head percentage : {}\nTail percentage : {}".format(int(head_count/percent_count*100),int(tail_count/percent_count*100)))
# print(f"Head percentage : {int(head_count/percent_count*100)}\n  Tail percentage : {tail_count/percent_count*100}")