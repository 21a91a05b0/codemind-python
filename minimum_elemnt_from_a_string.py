s=input()
a=s.split()
s=a[-1]
c=122
for i in s:
    if ord(i)<c:
        c=ord(i)
if chr(c).lower() in s:
    print(chr(c).lower())
else:
    print(chr(c))