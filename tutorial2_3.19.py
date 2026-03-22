def leap(year):
    return year %4==0 and ( year % 400==0 or year%100!=0)

def days_in_month(month, year):
    x=0
    if leap(year):
        x=1
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month == 2:
        return 28+x
    else:
        return 30

def decide(day, month, year):
    return 0 < day <= days_in_month(month, year)

def compare(d1,m1,y1,d2,m2,y2):
    j1 = y1*100000+m1*100+d1
    j2 = y2*100000+m2*100+d2
    return j1<j2
# making dates like 19001112 ez to judge

def count_seconds(s1,m1,h1,s2,m2,h2):
    time1=h1*3600+m1*60+s1
    time2=h2*3600+m2*60+s2
    return time2-time1

def count_seconds_further_days(s1,m1,h1,s2,m2,h2):
    if count_seconds(s1,m1,h1,s2,m2,h2) > 0:
        return count_seconds(s1,m1,h1,s2,m2,h2)
    else：
        return count_seconds(s1,m1,h1,s2,m2,h2+24)

# or another way to do this, no matter whether they are in the same day
def count_seconds_both(s1,m1,h1,s2,m2,h2):
    return count_seconds(s1,m1,h1,s2,m2,h2+24) %86400

"""
test line
"""
print(compare(19,12,1900,1,3,1901))
print(count_seconds_further_days(1,3,19,1,3,19))
print(count_seconds(1,3,19,1,3,19))
