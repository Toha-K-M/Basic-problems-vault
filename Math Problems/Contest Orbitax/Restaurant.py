
n1 = 2
n2 = 2

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

print("max: ", int((n1*n2) / (g*g)) )
