
graph = ['','A','B','C','D','E','F','G','H','S']
ar = [[0],[2,9],[1],[4,5,6,9],[3],[3,8],[3,7],[6,8,9],[7],[1,3,7]]
visited = []
s=[]

i = 0
s.append(1)
visited.append(1)

while not s == []:
    for i in ar[s[-1]]:
        if i not in visited:
            s.append(i)
            visited.append(i)
            break
        else:
            if i is ar[s[-1]][-1]:# check kortesi i list er last value kina
                s.remove(s[-1])

print(visited)

for i in visited:
    print(graph[i],end=" ")
