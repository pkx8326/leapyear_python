#Leap year conditions:
#1. If a year is divisible by 4, it is a leap year, unless it is also divisible by 100. That means that if it is divisible by 4 but (AND) indivisible by 100, it is a leap year.
#2. If the year doesn't fulfill the first condition, for example, if it is divisible by 4 but also divisible by 100, it also has to be divisible by 400 to be a leap year,
#otherwise it is not.

year = int(input("Which year do you want to check? "))

if year % 4 == 0 and year % 100 != 0:
    print("Leap year.")       
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
