import calendar
import time

# printing header of the week, starting from Monday
print(calendar.weekheader(9) + "\n")

# printing calendar for the a particular month of a year along with spacing between each day
print(calendar.month(2020, 4) + "\n")

# printing a particular month in 2-D array mode
print(calendar.monthcalendar(2020, 4))
print()

# printing calendar for the entire year
print(calendar.calendar(2020))
print()

# printing a particular day of the week in a month in terms of integer
print(calendar.weekday(2020, 4, 12)) # answer is 6, because according to python 6 is Sunday
print()

# finding whether a year is leap year or not
print(calendar.isleap(2020))
print()

# finding leap days within specific years, the year you put at the end is exclusive, 2000 and 2004 is leap year.
print(calendar.leapdays(2000,2005))
