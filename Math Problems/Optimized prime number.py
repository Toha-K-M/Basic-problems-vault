import time
start_time = time.time()
####################################################
import math
print("enter a number: ")
n = int(input())
rooted = int(math.sqrt(n))

if n <= 1:
    print("not prime")
elif n == 2 or n == 3:
    print("prime")
elif n % 2 == 0:
    print("not prime")
else:
    for i in range(3,rooted,2):
        if(n % i == 0):
            print("not prime")
            break
        else:
            print("prime")
            break
#####################################################
end_time = time.time() - start_time
print(end_time)
