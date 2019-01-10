import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import math
k = '''0.98 0.92 0.89 0.90 0.94 0.99 0.86 0.85 1.06 1.01
1.03 0.85 0.95 0.90 1.03 0.87 1.02 0.88 0.92 0.88
0.88 0.90 0.98 0.96 0.98 0.93 0.98 0.92 1.00 0.95
0.88 0.90 1.01 0.98 0.85 0.91 0.95 1.01 0.88 0.89
0.99 0.95 0.90 0.88 0.92 0.89 0.90 0.95 0.93 0.96
0.93 0.91 0.92 0.86 0.87 0.91 0.89 0.93 0.93 0.95
0.92 0.88 0.87 0.98 0.98 0.91 0.93 1.00 0.90 0.93
0.89 0.97 0.98 0.91 0.88 0.89 1.00 0.93 0.92 0.97
0.97 0.91 0.85 0.92 0.87 0.86 0.91 0.92 0.95 0.97
0.88 1.05 0.91 0.89 0.92 0.94 0.90 1.00 0.90 0.93'''

k = k.replace(" ",",")
k = k.replace("\n",",")
k = k.split(',')

n = []
#classes
for i in k:
    n.append(float(i))
    
max = max(n)
min = min(n)
k = 8
range = max - min
interval = range/k
interval = math.ceil(interval)
interval = .03

start = .835
fi = [0]*8
for i in n:
    if start >= i and i <= start+interval:
        fi[0] += 1
    elif start + interval>= i and i <= start+interval:
        fi[1] += 1
    elif start >= i and i <= start+interval:
        fi[2] += 1
    elif start >= i and i <= start+interval:
        fi[3] += 1
    elif start >= i and i <= start+interval:
        fi[4] += 1
    elif start >= i and i <= start+interval:
        fi[5] += 1
    elif start >= i and i <= start+interval:
        fi[6] += 1
    else:
        fi[7] += 1

'''incremented .03'''

fi = [7,20,27,18,14,9,3,2]

print(fi)

hx = []
for i in fi:
    hx.append(i/(interval*len(n)))
print(hx)
# for i in n:
#     class_marks = (max(interval) - min(interval))/2
hx=[2.3,6.6,9,6.0,4,6,3.1,.6]
width = 1/1.5
class_mark = [.85,.88,.91,.94,.97,1.00,1.03,1.06]
plt.bar(class_mark, hx, label='Concentrations of fluoride in toothpaste',align='center')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.legend()
plt.show()

plt.bar(class_mark, fi, label='Concentrations of fluoride in toothpaste',align='center')
df = sns.load_dataset()
plt.xlabel('x')
plt.ylabel('frequency')
plt.legend()
plt.show()

plt.boxplot(n)
plt.show()


plt.bar(class_mark, fi, label='Concentrations of fluoride in toothpaste',align='center', color='r')
plt.bar(class_mark, hx, label='Concentrations of fluoride in toothpaste',align='center')
plt.xlabel('x')
plt.ylabel('h(x) and frequency')
plt.show()