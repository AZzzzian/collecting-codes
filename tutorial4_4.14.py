def calculate(num):
    if num == 0:
        return 1
    else:
        return num * calculate(num-1)

def decide_special(n):
    if n == 0:
        return 0
    else:
        return n == calculate(n%10) + decide_special(n//10)

def cal_difference(x,num):
    return (num - x)**2

def find_index(x,array):
    i=0
    index = 0
    dif=cal_difference(x,array[i])
    while i!=len(array):
        if cal_difference(x,array[i])<dif:
            dif=cal_difference(x,array[i])
            index=i
        i=i+1
    return index

def reverse_part(array,i1,i2):
    i=0
    while i!=(i2-i1+1)//2:
        array[i1+i],array[i2-i]=array[i2-i],array[i1+i]
        i=i+1
    return array

def decide_reverse_index(array):
    i=1
    index1=0
    index2=len(array)-1
    while i!=len(array)-3:
        if array[i]<array[i+1] and array[i-1]<array[i]:
            index2=i
        if array[i]>array[i+1] and array[i-1]<array[i]:
            index1=i
        i=i+1
    re_array=reverse_part(array,index1,index2)
    print(re_array)

def decide_is_ascending(array):
    i=0
    while i!=len(array) and array[i]<array[i-1]:
        i=i+1
    return array[i]<array[i-1]





# print(calculate(5))
# print(decide_special(145))
# print(find_index(97,[1,2,3,45,100,6,9,99,77,44]))
array2=[0,1,2,6,5,4,3,7,8,9]
decide_reverse_index(array2)
print(decide_is_ascending(array2))

#
"q1"
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

"q2 i increasing part, j decreasing, k increasing "
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


"q3: s means enter time, e means leave time"
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


"not in tutorial, O(log(n))"
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












