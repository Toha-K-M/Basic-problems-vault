class v:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

a = v('a',20)
b = v('b',10)
c = v('c',15)

li = [a,b,c]
sorted_list = sorted(li, key=lambda v:v.weight) # sorting object weight attribute nie
for i in sorted_list:
    print(i.name, "=", i.weight)