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

def rotate(array):
    i=1
    new=[]
    while i!=len(array):
        new.append(array[i])
        i=i+1
    new.append(array[0])
    return new
def rotate_right(array):
    i=0
    current=array[0]
    while i!=len(array):
        temp=array[(i+1)%len(array)]
        array[(i+1)%len(array)]=current
        current=temp
        i=i+1



print(rotate([1,2,1,3,9,4,8,6,5,0]))



print(rotate([1,2,1,3,9,4,8,6,5,0]))
