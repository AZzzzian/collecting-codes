if __name__ == '__main__':
    print("By Zian , collecting codes from Herry, also something originated by myself,and add stars plz ozn")

"""
question1: replace the digit inside the number and find "0"s
"""

def replace_digits(a,b,c):
    if a==c:
        return b
    else:
        return c

def replace(x,y,n):
    if 0<n<10:
        return replace_digits(x,y,n)
    else:
        return replace(x,y,n//10)*10+replace_digits(x,y,n%10)

def trailing_zeros(n):
    count=0
    while n!=0 and n%10==0:
        count=count+1
        n=n//10
    return count

"""
question2: count days from 1900 and print out the day

i dont like the code he gave us, so i wrote another
ps: teacher didn't want us to use list or sth ,but i can't stand with that
"""
def print_day_trash(n):

    if n%7==1:
        print("Monday")
    if n%7==2:
        print("Tuesday")
    if n%7==3:
        print("Wednesday")
    if n%7==4:
        print("Thursday")
# that's bullshit u can try this


def print_day(n):
    print (["monday","tuesday","wednesday","thursday","friday","saturday","sunday"][n%7-1])

def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def full_years(n):
    total=0
    i=1900
    while i!=n:
        if leap(i):
            total= total+366
        else:
            total=total+365
        i=i+1
    return total

def max_days(m, y):
    x = 0
    if leap(y):
        x = 1
    if m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif m == 2:
        return 28 + x
    else:
        return 30

def full_months(m,y):
    total=0
    i=1
    while i!=m:
        total= total + max_days(i, y)
        i=i+1
    return total

def days_total(d,m,y):
    return full_years(y)+full_months(m,y)+d


"""
another question: count days between two valid date d1m1y1 and d2m2y2
"""

def count_days(d1,m1,y1,d2,m2,y2):
    return days_total(d2,m2,y2)-days_total(d1,m1,y1)

"""
homework: 8 friends order their favorite dished at a round table, could rotate the table to at least 2 of them get their dishes

well we didn't have to use code to explain this, simple as it seem. A round table contian 8 angles (I mean there are 8 angles to rotate) and the first angle doesn't fit anyone,
so, the 8 people's favorite dish must be achieved from the the left 7 angles, and that means, there exists one rotate satisfied at least 2 people
EZPZ :D
"""



"""
tets line
"""

print(replace(1,2,111111))
print_day(5)
