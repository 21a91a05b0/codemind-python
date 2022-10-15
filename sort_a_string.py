a=input()
l=[]
b=''
c=[]
z=[]
for i in range(len(a)):
    if a[i].isalnum():
        b+=a[i]
    else:
        l.append(i)
        z.append(a[i])
b=sorted(b)
for i in range(len(l)):
    b.insert(l[i],z[i])
print(''.join(b))