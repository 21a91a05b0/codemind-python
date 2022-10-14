def isprime(x:int)->bool:               
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
            break
    else:
        return True
n=int(input())
m=int(input())
a=n+m
temp=a
while True:
    if (isprime(a+1)):
        y=a+1
        break
    a+=1
print(y-temp)