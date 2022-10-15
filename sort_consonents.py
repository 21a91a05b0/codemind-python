def sort(n):
    a=[]
    b=[]
    c=[]
    v='aeiou'
    for i in range(len(n)):
        if n[i] in v:
            a.append(i)
            b.append(n[i])
        else:
            c.append(n[i])
    c=sorted(c)
    for i in range(len(a)):
        c.insert(a[i],b[i])
    return ''.join(c)
s=input()
for i in s.split():
    print(sort(i),end=' ')