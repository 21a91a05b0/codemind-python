n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
b=set(a)
for i in b:
    if i%2!=0 and i!=0:
        s+=1
print(s) 