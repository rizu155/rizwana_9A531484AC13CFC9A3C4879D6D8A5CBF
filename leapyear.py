#Find Leap year
def leapYear(y):

  if y % 4 == 0:
    if y % 100 != 0:
      return True
    elif y % 400 == 0:
      return True
    else:
      return False


y = int(input("ENTER THE YEAR:"))

if leapYear(y):
  print("{} is a leap year .".format(y))

else:
  print("{} is not a leap year .".format(y))
