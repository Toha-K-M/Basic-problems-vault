import time
start_time = time.time()
######################################
print("enter how many numbers:")
n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
a = sorted(a)

def gcd(a, b):
    if(b == 0):
        return a
    if(a % b == 0):
        return b
    return gcd(b, a % b)

g = gcd(a[0],a[1])
l = (a[0] * a[1])/g
if n > 2:
    for i in range(2,n):
        g = gcd(g,a[i])
        l = (l * a[i])/g
# euclid's algorithm for i in
print()
print("Euclid's Algorithm ")

print("GCD: ", g)
print("LCM: ", l)


#####################################################
end_time = time.time() - start_time
print("##############################################")
print("End Time: ", end_time)
