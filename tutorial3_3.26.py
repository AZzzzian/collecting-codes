import random


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
codes downside is without using new list, i pack these2 process( pick 0 and sort) into a new function
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
test
"""

random_list=create_more0_array()
print("before:",random_list)
print()
print("after:",sort_array(random_list))
print()

random_list=create_more0_array()
print("before:",random_list)
print()
print("after pick 0:",pick_zero(random_list))
print()
print(pick_zero_right(random_list))