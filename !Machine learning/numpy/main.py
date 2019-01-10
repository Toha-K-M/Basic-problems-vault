import time
import numpy as np

list = [1,2,3]

a = np.array(list)

print(a)

print(list + list)

print(a + a, a * a)

print(np.sqrt(a))

print(np.log(a))

print(4 * a)

n_features = 10000000

x = np.random.uniform(0,1,(n_features,1))
w = np.random.randn(1,n_features)
b = 0
print(x,w)

x1 = x[:,0].tolist()
w1 = w[0,:].tolist()

print(x1,w1)

start = time.time()
z = 0

for i in range(n_features):
    z = z+x1[i]*w1[i]

z = z+b

list_result = z

end = time.time()
t1 = (end - start)*1000

print(t1)

start = time.time()

z = np.dot(w,x) + b
end = time.time()

t2 = (end-start) * 1000
result = z[0,0]

print(t2)