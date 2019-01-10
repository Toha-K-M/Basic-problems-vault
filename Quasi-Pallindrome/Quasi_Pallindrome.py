
t = input()
val = []
flag = 0
count = 0


for i in str(t):
    val.append(i)

for j in reversed(val):
    if (j == "0" and flag == 0):
        #print j
        count += 1
    if (j != "0"):
        flag = 1
#print count

t = str(t)
#print len(t)-count
if t[:len(t)-count] == str(t)[len(t)-count-1::-1]:
    print "YES"
    #print t[0:len(t)-count]
else:
    print "NO"
   # print str(t)[len(t)-count-1::-1]














