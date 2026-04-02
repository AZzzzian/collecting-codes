import random
"""
note:
i == "start index"
result = "start result"
while(i!=end):
    result= "result combined with f[i]"
    i=i+1
"""
def sum_1(array):
    i=0
    sum1=0
    while i!=len(array):
        sum1=sum1+array[i]
        i=i+1
    return sum1

def count_even(array):
    i=0
    count=0
    while i!=len(array):
        if array[i]%2==0:
            count=count+1
        else:
            count=count
        i=i+1

def mix_ascending(g,f):
    i,j=0,0
    array=[]
    while i!=len(f) and j!=len(g) :
        if f[i]<g[j]:
            array.append(f[i])
            i=i+1
        elif f[i]>g[j]:
            array.append(g[j])
            j=j+1
        else:
            array.append(f[i])
            array.append(g[j])
            j=j+1
            i=i+1
    if i==len(f):
        array=array+g[j:]
    else:
        array=array+f[i:]
    return array


"""
[1,2,3,4,5,6,7]
henry's codes down here, but I switch "size" to "len()",dont use len()
"""
def array_swap(array,i,j):
    array[i], array[j] = array[j], array[i]
def rotate_right_1_place(array):
    i=len(array)-1
    while i!=0:
        array_swap(array,i,i-1)
        i=i-1

def rotate_right(array,n):
    i=0
    while i!=n:
        rotate_right_1_place(array)
        i=i+1

def rotate_left_1_place(array):
    i=0
    while i!=len(array)-1:
        array_swap(array,i,i+1)
        i=i+1

def rotate_left(array,n):
    i=0
    while i!=n:
        rotate_left_1_place(array)
        i=i+1

def rotate(array,n):  #n>0 means rotate right
    if n>0:
        rotate_right(array,n)
    else:
        rotate_left(array,-n)
    return array

"""
test        
"""
print(rotate([1,2,3,4,5,6,7],2))
print(mix_ascending([1,2,3,4,5,6,7,8,9,10,20,40,50,55,65,75,80],[2,4,6,8,10,12,14,16,18,20]))

