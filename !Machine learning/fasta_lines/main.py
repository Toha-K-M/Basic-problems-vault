
# t = 't.txt'
# tx = open(t,"r")
# x = []
# for line in tx:
#     if '>' in line:
#         x.append(line.replace("\n",""))
#
# print(x)
#
# for i in range(0,len(x)):
#     print(i)

import os

this_folder = os.path.dirname(os.path.abspath(__file__))
t = os.path.join(this_folder,'t.txt')

tx = open(t,'r')

x = []
for line in tx:
    if '>' in line:
        x.append(line.replace("\n",""))

print(x)
gm
# for i in range(0,len(x)):
#     print(i)
