#Euclid's Algorithm


def gcd (x,y):
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x
    return x

def print_missing(f,size):
    i=0
    while i!=size:
        j=f[i]
        while f[i]!=f[j]:
            f[i],f[j]=f[j],f[i]
            j=f[i]
        i=i+1
    i=0
    while i!=size:
        if f[i]!=i:
            print(f[i],end=' ')
        i=i+1

def read_matrix(f,row,col):
    i=0
    while i!=len(f):5.13.py
        j=f[i]

def display_matrix(f,row,col):
    i=0
    while i!=row:
        j=0
        while j!=col:
            print(f[i][j],end=" ")
            j=j+1
            print()
        i=i+1

def add_matrix(A,B,row,col):
    new_matrix = []
    i=0
    while i!=row:
        new_row=[]
        j=0
        while j!=col:
            new_row.append(A[i][j]+B[i][j])
            j=j+1
        new_matrix.append(new_row)
    return new_matrix

def multiply_matrix(A,B,rowA,colA,rowB,colB):
    new_matrix = []
    i=0
    while i!=rowA:
        new_row=[]
        j=0
        while j!=colB:
            x=0
            value=0
            while x!=colA:
                value = value+ A[i][x]*B[x][j]
                x=x+1
            new_row.append(value)
            j=j+1
        i = i+1
        new_matrix.append(new_row)
    return new_matrix


def find_longest_even(f):
    def even(n):
        return n%2==0
    def odd(n):
        return n%2==1
    n,best,current = 0,0,0
    i=0
    while n!=len(f):
        if even(f[i]):
            n,best,current = n+1,max(current+1,best),current+1
        elif odd(f[n]):
            n,current = n+1,0
