
T = input()
n = map(int, raw_input().split())
maximum = 0

for i in range(0,T):
    count_for_one = 0
    if n[i] == 1:
        for j in range(0,i):
            if n[j] == 0:
                count_for_one += 1
        for k in range(i, T):
            if n[k] == 1:
                count_for_one += 1
    maximum = max(maximum,count_for_one)

for i in range(0,T):
    count_for_zero = 0
    if n[i] == 0:
        for j in range(0,i+1):
            if n[j] == 0:
                count_for_zero += 1
        for k in range(i+1, T):
            if n[k] == 1:
                count_for_zero += 1
    maximum = max(maximum,count_for_zero)

print maximum

