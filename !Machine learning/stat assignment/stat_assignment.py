import random
import matplotlib.pyplot as plt
# Actual Math
A = 1/6
B = (1-1/6)
AUB = A + B
print("P(A)=", A,"P(B)=", B,"P(AUB)=", AUB)

#Developed code for experiment
count = 0
other_count = 0
n = int(input())
p_count = []
p_other_count = []
p_union_count = []
for i in range(0,n):
    X = random.randrange(1,7)
    if i is 0:
        continue
    print(X)
    if X is 3:
        count += 1
    else:
        other_count += 1
    p_count.append(count/i)
    p_other_count.append(other_count/i)
    p_union_count.append((count/i) + (other_count/i))

print("Actually observing 3:", count)
print("Actual observation ratio: ", count/n)
print("Actually not observing 3:", other_count)
print("Actually not observing 3 ratio:", other_count/n)
# graph
n_range = list(range(0,n-1))
print(n_range)
plt.plot(n_range,p_count)
plt.xlabel("Event A")
plt.ylabel("relative frequency")
plt.show()

plt.plot(n_range,p_other_count)
plt.xlabel("Event B")
plt.ylabel("relative frequency")
plt.show()

plt.plot(n_range,p_union_count)
plt.xlabel("AUB")
plt.ylabel("relative frequency")
plt.show()


