a=int(input())
v=0
for j in range(a):
    s=input()
    for i in range(1,len(s)-1):
        if s[i]=='-' and s[i+1]=='-' or s[i-1]=='-' and s[i]=='-':
            v-=1
        elif s[i]=='+' and s[i+1]=='+' or s[i-1]=='+' and s[i]=='+':
            v+=1
print(v)