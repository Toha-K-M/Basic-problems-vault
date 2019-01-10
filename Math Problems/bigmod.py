print("enter number: ")
a = int(input())
print("enter power: ")
b = int(input())
print("enter mod: ")
M = int(input())

def bigmod(a,b,M):
    if b is 0: return 1 % M # return 1
    print(b)
    x = bigmod(a,int(b/2),M)
    x = (x * x) % M
    if b % 2 is 1: # if odd
        x = (x * a) % M
    print(x)
    return x

print(bigmod(a,b,M))

# also there is a binary approach