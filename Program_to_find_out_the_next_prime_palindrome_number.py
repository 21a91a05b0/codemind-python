def isprime(x:int)->bool:               
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
            break
    else:
        return True
def palindrome(n):
    sum=0
    temp=n
    while n>0:
        d=n%10
        sum=sum*10+d
        n//=10
    if sum==temp:
        return True
    else:
        return False
n=int(input())
while True:
    if (isprime(n+1) and palindrome(n+1)):
        print(n+1)
        break
    n+=1