year = 2000

 year = int(input("Enter a year: "))     # To get year (integer input) from the user

# divided by 100 means century year (ending with 00)
if (year % 400 == 0) and (year % 100 == 0):    # century year divided by 400 is leap year
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
elif (year % 4 ==0) and (year % 100 != 0):   # year divided by 4 is a leap year
    print("{()
