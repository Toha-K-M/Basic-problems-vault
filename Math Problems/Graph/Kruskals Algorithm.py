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

## including all edge in list to sort
arr = [ba,ac,ad,ce,de]
graph = []

## sorting
li = sorted(arr, key=lambda edge:edge.weight)

# first min edge
min_weighed_edge = li[0]
min_weighed_edge.visited = True # marked edges
min_weighed_edge.ver[0].visited = True # marked 1st Vertix of edge
min_weighed_edge.ver[1].visited = True # marked 2nd vertex of edge
graph = [min_weighed_edge.ver[0].name, min_weighed_edge.ver[1].name] # building graph : vertices only

###### starting the algorithm ############

e = [min_weighed_edge]  # for edges
li.remove(li[0])
while not len(graph) is 5: # here 4 is the number of total vertices
    if not li[0].visited:
        if li[0].ver[0].visited is False or li[0].ver[1].visited is False: # edge er j kono ekta vertex or 2 ta vertexi visited na hole # loop avoiding
            e.append(li[0])
            if li[0].ver[0].name not in graph:
                graph.append(li[0].ver[0].name)
            if li[0].ver[1].name not in graph:
                graph.append(li[0].ver[1].name)
            #marking as visited edge, vertices
            li[0].visited = True
            li[0].ver[0].visited = True
            li[0].ver[1].visited = True
    li.remove(li[0]) # removing from list

for i in e:
    print(i.name, " : ", i.weight)

for i in graph:
    print(i)