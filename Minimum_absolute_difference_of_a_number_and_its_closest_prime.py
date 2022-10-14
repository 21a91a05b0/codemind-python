def prime(n):
    if n==1 or n==0:
        return False
    else:
        for i in range(2,n//2):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
if prime(n):
    print(0)
else:
    for i in range(n,(2*n)+1):
        if prime(i):
            a=i
            break
    for i in range(n,1,-1):
        if prime(i):
            b=i
            break
    if abs(n-b)>abs(n-a):
        print(abs(n-a))
    else:
        print(abs(n-b))