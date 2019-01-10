class vertex:
    visited = False
    def __init__(self,name,adjacent,edges):
        self.name = name
        self.adjacent = adjacent #here list
        self.edges = edges
    def isVisited(self):
        self.visited = self.visited

class edge:
    visited = False
    def __init__(self,name,ver,weight):
        self.name = name
        self.ver = ver
        self.weight = weight
    def isVisited(self):
        self.visited = self.visited

a = vertex('a',[],[])
b = vertex('b',[],[])
c = vertex('c',[],[])
d = vertex('d',[],[])
e = vertex('e',[],[])

#adjacent adding
a.adjacent = [b,c,d]
b.adjacent = [a]
c.adjacent = [a,e]
d.adjacent = [a,e]
e.adjacent = [c,d]

ba = edge('ba',[b,a],0)
ac = edge('ac',[a,c],20)
ad = edge('ad',[a,d],40)
ce = edge('ce',[c,e],30)
de = edge('de',[d,e],60)

a.edges = [ba,ac,ad]
b.edges = [ba]
c.edges = [ac,ce]
d.edges = [ad,de]
e.edges = [ce,de]

## using DAC min to find the lowest weight
arr = [ba,ac,ad,ce,de]
left = 0
right = len(arr)-1

def find_min(li,left,right):
    if left is right:
        return li[left]
    mid = int((left+right)/2)
    min1 = find_min(li,left,mid)
    min2 = find_min(li,mid+1,right)
    return min1 if min1.weight < min2.weight else min2

min_weighed_edge = find_min(arr,left,right)
# print("Minimum Weight: ",min_weighed_edge.weight)
min_weighed_edge.visited = True
###### starting the algorithm ############
prim_graph = [] # main graph ekhane jabe
q = []

# minimum edge marking
for i in min_weighed_edge.ver:
    i.visited = True   # vertex of minimum edge marking
    prim_graph.append(i.name) # graph build
    q.append(i)
e = [min_weighed_edge]  # for edges
while not len(prim_graph) is 5: # here 4 is the number of total vertices
    temp = []
    for j in q:
        for i in j.edges:
            if not i.visited:
                temp.append(i) # temp array te q list er vertex er unvisited edge rakhtesi
                # print(i.weight)
    if not temp == []: # jodi unvisited edge thake na thakle removing from q
        # print(len(temp))
        min_weighed_edge = find_min(temp,0,len(temp)-1)
        min_weighed_edge.visited = True # min paoar pore marking edge as visited
        e.append(min_weighed_edge)
        # print(min_weighed_edge.name)
        for i in min_weighed_edge.ver:
            if not i.visited:    # ebar min edger er unvisited vertex ber korlam
                q.append(i) #unvisited vertex q te
                i.visited = True # unvisited vertex visited korlam
                prim_graph.append(i.name) # graph build

# print(prim_graph)
# for i in q:
#     print(i.name)
for i in e:
    print(i.name, " : ", i.weight)

