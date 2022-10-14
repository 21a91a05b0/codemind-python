n=int(input())
temp=n
fir=0
sec=1
l=[0,1]
while temp:
    sum=fir+sec
    fir=sec
    sec=sum
    l.append(sum)
    temp-=1
for i in range(n,2*n+1):
    if i in l:
        front=i
        break
for i in range(n,-1,-1):
    if i in l:
        back=i
        break
if (n-back)<(front-n):
    print(back)
elif (n-back)>(front-n):
    print(front)
else:
    print(back,front)