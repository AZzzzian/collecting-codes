
def decide_half_is_copy(array):
    i=0
    while i != 50:
        if array[i] != array[i+50]:
            return False
        i += 1
    return True

def decide_palindrome(array):
    i=0
    while i != 50:
        if array[i] != array[99-i]:
            return False
        i += 1
    return True

def reverse_array(array):
    i=0
    while i!=50:
        array[i], array[99-i] = array[99-i], array[i]
        i += 1

def reverse_part_of_array(array,index1,index2):
    i=0
    while index1+i<=index2-i:
        array[index1+i], array[index2-i] = array[index2-i], array[index1+i]
        i = i + 1


"""
H's

20134
20143

20314
20341

54321
54312
54231
54213
54132
54123



"""


def decide_half_copy(array):
    i=0
    while array[i]==array[i+50] and i!=49:
        i=i+1
    if array[i]!=array[i+50]:
        print("Not a copy")
    else:
        print("Is a copy")


def is_a_palindrome(array):
    i=0
    while array[i]==array[99-i] and i!=49:
        i=i+1
    if array[i]!=array[99-i]:
        print("Not a palindrome")
    else:
        print("Is a palindrome")

def reverse_section(array,i1,i2):
    i=0
    stop= ((i2-i1)+1)//2
    while i!=stop:
        array[i1+i], array[i2-i] = array[i2-i], array[i1+i]
        i = i + 1

def insertion_sort(f):
    i=0
    while i!=100:
        j=i
        while j!=0 and f[j-1]>f[j]:
            f[j],f[j-1]=f[j-1],f[j]
            j=j-1
        i=i+1

def selection_sort(array):
    i=0
    while i!=100:
        j=i
        min_index=i
        while j!=100:
            if array[j]<array[min_index]:
                min_index=j
            j = j+1
        array[i], array[min_index] = array[min_index], array[i]
        i=i+1

