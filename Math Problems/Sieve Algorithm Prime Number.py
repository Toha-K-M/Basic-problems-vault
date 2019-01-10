import time

start_time = time.time()
######################################
import math
n = 50
prime = [2]

limit = int(math.sqrt(n))

mark = [0]*100
mark[0] = 1
mark[1] = 1

for i in range(2,n+1,2):
    mark[i] = 1

for i in range(3,n+1,2):
    if(mark[i]==0):
        prime.append(i)
        if(i <= limit):
            for j in range(i*i,n+1,i*2): # ekhane i * 2 dara just odd gula mark kora hocche as even gulo agei line 15 e mark kora hoye gese
                mark[j] = 1

print(mark)
print(prime)
print("Not Prime: ")
for index,item in enumerate(mark):
    if item == 1:
        print(index)
######################################
end_time = time.time() - start_time