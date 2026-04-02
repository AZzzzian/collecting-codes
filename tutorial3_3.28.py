import random

"""
q1:
Suppose you have a 100 element array which contains values, Write a program to decide if the 
array is sorted in ascending order
"""
def create_more0_array():
    i = 0
    random_list = []
    while i < 100:
        if random.random() < 0.2:
            random_list.append(0)
        else:
            random_list.append(random.randint(-100, 100))
        i=i+1
    return random_list


def decide_ascending_array(array):
    i=0
    while i!=len(array):
        if array[i]>array[i+1]:
            return False
        i=i+1
    return True
"""
q2:
Suppose you have a 100 element array which contains numbers. Write a program that will 
rearrange the values so that all of the negative values appear before all of the zeros and all of the 
zeros appear before all of the positive values
"""
def sort_array(array):
    i=0
    while i!=len(array)-1:
        j=0
        while j<len(array)-i-1:
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            j=j+1
        i=i+1
    return array
"""
q3:
Suppose you have a 100 element array called f which contains numbers. Write a program to 
rearrange the values in f so that all the non zero values are moved to the start of f and all the zero 
values are moved to the end of f. The non zero values must still be in the order in which they were 
at the beginning.
"""
def pick_zero(array):

    i=0
    x=0
    while i!=len(array):
        if array[i]==0:
            array[x],array[i]=array[i],array[x]
            x=x+1
        i=i+1
    new=sort_array(array[x:])
    new.extend(array[:x])
    return new

"""
codes downside here are function without creating new list, i pack these2 process( pick 0 and sort) into a new function
"""

def pick_zero_right(array):
    i=len(array)-1
    x=len(array)-1
    while i != -1:
        if array[i] == 0:
            array[x], array[i] = array[i], array[x]
            x = x - 1
        i = i - 1
    zero_index=0
    """
    here is to find 0'index
    """
    y=0
    while y!=len(array) and array[zero_index]!=0:
        if array[y]==0:
            zero_index=y
        y=y+1
    """
    now result likes [-3,4,-1,1,-5,0,0,0,0]
    do the same sort but before the 0 index
    """
    i = 0
    while i != zero_index-1:
        j = 0
        while j < zero_index-1-i:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j = j + 1
        i = i + 1
    return array

"""
well i guess you'd like to see another way out
here is the other code, avoiding too much loop

[2,4,6,0,-1,4,-3,9,0]
[0,4,6,0,-1,4,-3,9,2]
[0,9,6,0,-1,4,-3,4,2]
[0,-3,6,0,-1,4,9,4,2]

if u dont understand this, try to divide numbers into 3 groups."<0", "=0" and ">0" 
"""
def sort(array):
    high=len(array)-1
    mid=0
    slow=0
    while mid<=high:
        if array[mid]<0:
            array[slow],array[mid]=array[mid],array[slow]
            mid=mid+1
            slow=slow+1
        elif array[mid]==0:
            mid = mid + 1
        else:
            array[high], array[mid] = array[mid], array[high]
            high = high - 1
    return array

"""
just changing the group will be enough to solve both q2 and q3
"""
def sort_pick0(array):
    high = len(array) - 1
    mid = 0
    slow = 0
    while mid <= high:
        if array[mid] < 0:
            array[slow], array[mid] = array[mid], array[slow]
            mid = mid + 1
            slow = slow + 1
        elif array[mid] > 0:
            mid = mid + 1
        else:
            array[high], array[mid] = array[mid], array[high]
            high = high - 1
    return array

"""
also, 3 pointers will be stressful dealing this, we can use 2 pointers
"""
def sort_pointer2(array):
    left=0
    mid=0
    while mid != len(array):
        if array[mid] < 0:
            array[left], array[mid] = array[mid], array[left]
            left = left + 1
            mid = mid + 1
        else:
            mid = mid + 1
# ofcourse I'm not necessary using else here, but it's more able to understand
# now we got all negative numbers left side, then we process right side
    right=len(array)-1
    mid=0
    while mid <= right:
        if array[mid] > 0:
            array[right], array[mid] = array[mid], array[right]
            right = right - 1
        else:
            mid = mid + 1
    return array
"""
so the last question ez as it seems now, i not gonna write it again, just changing the "group" will be enough
"""

"""
4.1
henry's codes i wrote down here
"""
def array_swap(g,i1,i2):
    g[i1], g[i2] = g[i2], g[i1]

def dutch_national_flag(array):
    i,j,k=0,0,len(array)
    while j!=k:
        if array[j]==0:
            j=j+1
        elif array[j]<0:
            array_swap(array, i, j)
            i,j=i+1,j+1
        elif array[j]>0:
            array_swap(array, j, k - 1)
            k=k-1
    return array
def dutch_national_flag_move0(array):
    i,j,k=0,0,len(array)
    while j!=k:
        if array[j]>0:
            j=j+1
        elif array[j]<0:
            array_swap(array, i, j)
            i,j=i+1,j+1
        elif array[j]==0:
            array_swap(array, j, k - 1)
            k=k-1
    return array
"""
test
"""

# random_list1=create_more0_array()
# print("before:",random_list1)
# print()
# print("after:",sort_array(random_list1))
# print()
#
# random_list2=create_more0_array()
# print("before:",random_list2)
# print()
# print("after pick 0:",pick_zero(random_list2))
# print()
# print(pick_zero_right(random_list2))

random_list3=create_more0_array()
print("before:",random_list3)
print()
print("after:",dutch_national_flag(random_list3))

random_list4=create_more0_array()
print("before:",random_list4)
print()
print("after:",dutch_national_flag_move0(random_list4))
