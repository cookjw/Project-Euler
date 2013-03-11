def nextdaymonth(month, day, year):
    if month in [1,3,5,7,8,10,12]:
        if day != 31:
            return [month, day + 1, year]
        elif month != 12:
            return [month + 1, 1, year]
        if day == 31 and month == 12:
            return [1,1, year + 1]
            
    if month in [4,6,9,11]:
        if day != 30:
            return [month, day + 1, year]
        else:
            return [month + 1, 1, year]
    if month == 2:
        if day <= 27 or (day <= 28 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
            return [month, day+1, year]
        else:
            return [month + 1, 1, year]
        

def nextday_year(month, day, year):
    if month == 12 and day == 31:
        return year + 1
    else:
        return year


def nextday(date):
    weekday = date[0]
    month = date[1]
    day = date[2]
    year = date[3]
    return [(weekday+1)%7, nextdaymonth(month, day, year)[0], nextdaymonth(month, day, year)[1], nextday_year(month, day, year)] 
    
date = [1, 01, 01, 1900]

datelist = []    
while date[3] <= 2000:
    datelist.append(date)
    date = nextday(date)
    
print len([x for x in datelist if x[3] >= 1901])

print len([x for x in datelist if x[3] >= 1901 and x[2] == 1 and x[0] == 0])

    
