
n = input()
people = 2*n
kayak = n-1
weight = [people]
weight = map(int,raw_input().split())
tot_weight = []
flag = 0
x = -1
y = 0
sum = 0
count = people - 1
while(count):
    x = x+1
    y = y+1
    flag = 0
    sum = 0
    for i in range(0, people - 1):
        if (i == x and i + 1 == y and flag == 0):
            sum = abs(weight[i] - weight[i + 1]) + sum
            x = i
            y = i + 1
            print x, y
            flag = 1
        if (i != x and i != y):
            sum = abs(weight[i] - weight[i + 1]) + sum
            x = i
            y = i + 1
            print x, y
            print sum
    count -= 1

print sum
# instability if i, j are single kayakers
