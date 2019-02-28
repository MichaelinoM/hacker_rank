def is_leap(year):
#    The year can be evenly divided by 4, is a leap year, unless:
#      The year can be evenly divided by 100, it is NOT a leap year,unless:
#          The year is also evenly divisible by 400. Then it is a leap year.

    a = year % 4
    b = year % 100
    c = year % 400
    if a ==0 and b!=0 and c!=0:
        leap = True
    elif a==0 and b==0 and c==0:
        leap = True
    else:
        leap = False
    # Write your logic here
    return leap

year = int(input())
