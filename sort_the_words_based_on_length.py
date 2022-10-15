s=input().split()
l=[]
for i in sorted(s):
    x=len(i)
    l.append(x)
a=min(l)
b=max(l)
l=[]
while a<=b:
    c=0
    for i in sorted(s):
        if len(i)==a:
            l.append(i)
    a+=1
print(' '.join(l))