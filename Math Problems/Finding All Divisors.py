import time
start_time = time.time()
######################################
import math
n = 20
limit = int(math.sqrt(n))

divisors = []
for i in range(1,limit+1):
    if n % i == 0:
        divisors.append(i)
        if(i != n/i):
            divisors.append(n/i)

print(divisors)
#####################################################
end_time = time.time() - start_time
print(end_time)
