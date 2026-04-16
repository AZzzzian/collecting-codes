#H's code, he didnt show answer for q0 
"q1:Given f, a 100 element array containing integers, and x an integer, find the index i in f where f[i] is closest to x."
def difference(x,y):
    if x<=y:
        return y-x
    else:
        return x-y
def closest_index(f,x):
    i,best=0,0
    while i!=100:
        if difference(f[i],x)<=difference(f[best],x):
            best=i
        i=i+1
    print(best)

"q2:Given f, a 100 element array containing integers, write a program to decide if f could be sorted in ascending order just by reversing a part of f "
"i means increasing part, j decreasing, k increasing, maybe you can draw a line map to see it "
def dae(f):
    i,j,k=0,0,99
    while j!=k and f[i]<f[i+1]:
        i,j=i+1,j+1
    while j!=k and f[j]>f[j+1]:
        i,j=i+1,j+1
    while j!=k and f[k-1]<f[k]:
        k=k-1
    if j!=k:
        return False
    else:
        if i==99:
            print("all increasing")
            return True
        elif i==0 and j==99:
            print("all decreasing")
            return True
        elif i==0 and j!=99 and f[i] <f[j+1]:   # and f[i]<f[99]:
            print("1st part empty,can reverse 2nd part")
            return True
        elif i!=0 and j==99 and f[j] >f[i-1]:   # and f[i]<f[99]
            print("3rd part empty,can reverse 2nd part")
            return True
        elif i!=0 and f[i-1] <f[j-1] and f[i] <f[j+1]:
            print("reverse 2nd part")
            return True
        else:
            return False


"q3:We have 2 100 element arrays of positive integers, s and e."
" These records the time that people entered and left the library on a particular day.
"So person i entered at time s[i] and left at time e[i]. We are told that the array s is sorted in ascending order.  s means enter time, e means leave time"
def library_people(e,s):
    i=0
    latest=0
    total=0
    while i!=100:
        if e[i]<=latest:
            total,latest=total,latest
        elif s[i]<=latest and latest<e[i]:
            total,latest=total+e[i]-latest,e[i]
        elif latest<s[i]:
            total,latest=total+e[i]-s[i],e[i]
        i=i+1
    print(total)


"this is not in tutorial, a Bisection method didnt more than O(log(n))"
def odd(n):
    return n%2 != 0
def even(n):
    return n%2 == 0
def find_odd_and_even(f):
    i,j=0,99999
    while j!=i+1:
        h=(i+j)//2
        if odd(f[h]):
            i=h
        elif even(f[h]):
            j=h

"i am still working on the last problem he gave us"












