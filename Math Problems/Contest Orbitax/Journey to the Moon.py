np = input().split()

n = int(np[0])

p = int(np[1])

astronaut = []

for _ in range(p):
    astronaut.append(list(map(int, input().rstrip().split())))
###
visited = [0]*n
country = []
count = -1
for i in range(p):
    print("begin:" , visited)
    if visited[astronaut[i][0]] and visited[astronaut[i][1]]:
        if visited[astronaut[i][0]] != visited[astronaut[i][1]]:
            print("got ", astronaut[i][0], " : ", visited[astronaut[i][0]]  )
            print("got ", astronaut[i][1], " : ", visited[astronaut[i][1]]  )
            if visited[astronaut[i][0]] > visited[astronaut[i][1]]:
                temp = visited[astronaut[i][1]]
                temp1 = visited[astronaut[i][0]]
                for k in country[temp1-1]:
                    country[temp - 1].append(k)
                    visited[k] = temp
                del country[temp1-1]
                count -= 1
            else:
                temp = visited[astronaut[i][0]]
                temp1 = visited[astronaut[i][1]]
                for k in country[temp1 - 1]:
                    country[temp - 1].append(k)
                    visited[k] = temp
                del country[temp1 - 1]
                count -= 1
    elif visited[astronaut[i][0]] or visited[astronaut[i][1]]:
        print("elif:", visited)
        if visited[astronaut[i][0]]:
            temp = visited[astronaut[i][0]]
            country[temp-1].append(astronaut[i][1])
            visited[astronaut[i][1]] = temp
        else:
            temp = visited[astronaut[i][1]]
            country[temp - 1].append(astronaut[i][0])
            visited[astronaut[i][0]] = temp
    else:
        count += 1
        country.append([])
        country[count].append(astronaut[i][0])
        visited[astronaut[i][0]] = count + 1
        country[count].append(astronaut[i][1])
        visited[astronaut[i][1]] = count + 1

for i in range (n):
    if not visited[i]:
        count += 1
        visited[i] = count + 1
        country.append([i])

print(country)

total = 0
l = len(country)
for i in range(l):
    print('i + 1 :', i+1)
    if not i+1 is l:
        for j in range(i+1, l):
            total += len(country[i])*len(country[j])
            print(country[i], '*', country[j], ' : ', total)
print(visited)
print(total)


