if __name__ == '__main__':
    print("By Zian , collecting codes from Herry, also something originated by myself,and add stars plz ozn")

"""
q1:Given a date d, m, y, write a function to decide if this is a valid date
"""
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
"""
q2:Given 2 dates d1, m1, y1 and d2, m2, y2, write a function to decide if the second date is after the 
first date
"""
def compare(d1,m1,y1,d2,m2,y2):
    j1 = y1*100000+m1*100+d1
    j2 = y2*100000+m2*100+d2
    return j1<j2
# making dates like 19001112 ez to judge
"""
q3:Given 2 times on the same day on a 24 hour clock, h1, m1, s1 and a later time h2, m2, s2, write a 
program to determine how many seconds later the second time is.
"""
def count_seconds(s1,m1,h1,s2,m2,h2):
    time1=h1*3600+m1*60+s1
    time2=h2*3600+m2*60+s2
    return time2-time1
"""
q4:. Given 2 times on a 24 hour clock, h1, m1, s1 and a later time h2, m2, s2. The times  are less than 
24 hours apart but now the second time could be on the next day. Write a program to determine 
how many seconds after the first time later the second time is.
"""
def count_seconds_further_days(s1,m1,h1,s2,m2,h2):
    if count_seconds(s1,m1,h1,s2,m2,h2) > 0:
        return count_seconds(s1,m1,h1,s2,m2,h2)
    else:
        return count_seconds(s1,m1,h1,s2,m2,h2+24)
# or another way to do this, no matter whether they are in the same day
def count_seconds_both(s1,m1,h1,s2,m2,h2):
    return count_seconds(s1,m1,h1,s2,m2,h2+24) % 86400

#and this is the teacher's codes down here
def remaining_seconds(s):
    return 60-s
def seconds_in_minutes(ms,me):
    return (me-ms)*60
def seconds_in_hours(hs,he):
    return (he-hs)*3600
def seconds_ahead_today(s1,m1,h1,s2,m2,h2):
    if h1 == h2:
        if m1 == m2:
            return s2-s1
        else:
            return remaining_seconds(s1)+seconds_in_minutes(m1+1,m2) + s2
    else:
        return remaining_seconds(s1) + seconds_in_minutes(m1+1,60)+seconds_in_hours(h1+1,h2)+seconds_in_minutes(1,m2)+s2
def same_day(s1,m1,h1,s2,m2,h2):
    if h1 == h2:
        if m1 == m2:
            return s1==s2
        else:
            return remaining_seconds(s1)+seconds_in_minutes(m1+1,m2)+s2
    else:
        return remaining_seconds(s1)+seconds_in_minutes(m1+1,60)+seconds_in_hours(h1+1,h2)+seconds_in_minutes(1,m2)+s2

def seconds_ahead_tomorrow(s1,m1,h1,s2,m2,h2):
    return remaining_seconds(s1)+seconds_in_minutes(m1+1,60)+seconds_in_hours(h1+1,24)+seconds_in_hours(1,h2)+seconds_in_minutes(1,m2)+s2

def seconds_ahead(s1,m1,h1,s2,m2,h2):
    if same_day(s1,m1,h1,s2,m2,h2):
        return seconds_ahead_today(s1,m1,h1,s2,m2,h2)
    else:
        return seconds_ahead_tomorrow(s1,m1,h1,s2,m2,h2)



"""
test line
"""
print(compare(19,12,1900,1,3,1901))
print(count_seconds_further_days(1,3,19,1,3,1))
print(count_seconds(1,3,19,1,3,20))
print(seconds_ahead(1,3,19,1,4,20))