#leap year

"""
year%4==0&
year%100!==0/
year%400==0

"""
def is leap year (year):
if (year%4==0 and year%100!=0) or year%400==0:
  return True
else:
  return False

year=int(input("enter a year:"))

if is leap year ( year):
print ('{} is leap year.'. format ( year))
else:
print(' {} is not a leap year.'. format (year))
