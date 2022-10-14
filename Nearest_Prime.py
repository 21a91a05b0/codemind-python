def prime(i):
    if i==1:
        return 0
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
    if c==0:
        return i
m=int(input())
for i in range(m):
    n=int(input())
    for i in range(n,0,-1):
        if prime(i):
            l=i
            break
    for i in range(n+1,n*n):
        if prime(i):
            s=i
            break
    if (s-n)>=(n-l):
        print(l)
    else:
        print(s)