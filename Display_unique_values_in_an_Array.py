n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(n):
    s=0
    for j in range(n):
        if l[i]==l[j]:
            s+=1
    if s==1:
        print(l[i],end=' ')
        c+=1
if c==0:
    print("-1")