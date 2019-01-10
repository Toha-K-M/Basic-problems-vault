graph = ['','A','B','C','D','E','F','G','H','S']
ar = [[0],[2,9],[1],[4,5,6,9],[3],[3,8],[3,7],[8,6,9],[7],[1,3,7]]
visited = [] # jehetu 1 theke count korbo so 0 er jonno extra nisi 9 + 1 = 10
q=[]

i = 0
q.append(1)
visited.append(1)
# while not q == []:
#     if ar[q[0]][i] not in visited:
#         q.append(ar[q[0]][i])
#     if i is len(ar[q[0]]) - 1:
#         i = 0
#         if q[0] not in visited:
#             visited.append(q[0])
#         q.remove(q[0])
#     else:
#         i += 1
while not q == []:
    for i in ar[q[0]]:
        if i not in visited:
            q.append(i)
            visited.append(i)
    q.remove(q[0])
print(visited)

for i in visited:
    print(graph[i],end=" ")
