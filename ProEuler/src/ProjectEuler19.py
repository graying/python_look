'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def isLeapYear(year):
    if year == 2000:
        return True
    elif (year % 4) == 0:
        return True
    else:
        return False

aNum = 0
DaysTo19000101 = 365
# myDict = {}    
for Year in range(1901, 2001):
    for Month in range(1, 13):
        myDate = Year * 100 + Month
#       myDict[myDate] = DaysTo19000101
        
        weekDay = (DaysTo19000101 + 1) % 7
        # days +1 because 1901 01 01 is Monday
        if weekDay == 0:
            aNum += 1      
        print ("date={0} and days={1} and weekday={2}, total = {3}".format(myDate,
                                                              DaysTo19000101,
                                                              weekDay,
                                                              aNum))
        
        if Month in (1, 3, 5, 7, 8, 10, 12):
            DaysTo19000101 += 31
        elif Month in (4, 6, 9, 11):
            DaysTo19000101 += 30
        elif Month == 2 and isLeapYear(Year):
            DaysTo19000101 += 29
        else:
            DaysTo19000101 += 28