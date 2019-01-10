import time
start_time = time.time()
######################################
n1 = 12
n2 = 42

# normal way
print("Normal GCD")
for i in range(12,0,-1):
    if(42 % i == 0 and 12 % i == 0):
        print("gcd: ",i)
        break

# euclid's algorithm
print()
print("Euclid's Algorithm ")
if n1 > n2:
    a = n1
    b = n2
else:
    a = n2
    b = n1

def gcd(a, b):
    if(b == 0):
        return a
    if(a % b == 0):
        return b
    return gcd(b, a % b)

g = gcd(a,b)
print("gcd: ", g)
l = (n1 * n2)/g ### as rule n1 * n2 = gcd * lcd
print("lcd: ",l)
#####################################################
end_time = time.time() - start_time
print("##############################################")
print("End Time: ", end_time)
