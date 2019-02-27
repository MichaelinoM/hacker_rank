#!/bin/python3

N = int(input())

a = N % 2  #modulo (even number will have zero if divided by 2)

if a!=0:
    print("Weird")
elif a==0 and (N>1 and N<6):
    print("Not Weird")
elif a==0 and (N>5 and N<21):
    print("Weird")    
elif a==0 and (N>20):
    print("Not Weird")   
else:
    print("error")
