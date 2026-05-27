
def H_amount(N):
    coins=[100,50,20,10,5,2,1]
    i=0
    count=0
    while i!=0:
        if coins[i]<=N:
            count,N=count+1,N-coins[i]
        else:
            i=i+1
    return count




"when coins like [3,4,6,19],we should figure out whether the number can be made up"
def H(N):
    CV=[3,4,6,19]
    H=[]
    m=0
    i=0
    H.append(True)
    while m!=N:
        n,r=0,False
        while n!=len(CV):
            if CV[n]<=m+1:
                r=r or H[m+1-CV[n]]
            n=n+1
        m=m+1
        i=i+1
        H.append(r)
    print(H[m])

“”
test
“”
H(23)
H(25)
H(24)
H(1)
