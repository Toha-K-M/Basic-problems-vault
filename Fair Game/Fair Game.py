
n = input()
a = []
flag = 0
for i in range(0,n):
    a.append(input())

a.sort()

for i in range(1,n/2):
    if a[0]!=a[i]:
        flag = 1

if(flag == 0):
    for i in range(n/2 + 1, n):
        if a[n/2] != a[i]:
            flag = 1

if(flag == 0 and a[0]==a[n/2]):
    flag = 1

if(flag == 0):
    print "YES"
    print a[0],a[n/2]
else:
    print "NO"