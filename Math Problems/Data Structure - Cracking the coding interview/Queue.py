import queue

q = queue.Queue()

q.put(5)

print(q.get())

print(q.empty())

for i in range(5):
    q.put(i)

print("Queue Size : ", q.qsize())
print("Is Queue full: ", q.full())
print("First Item: ", q[0])
while not q.empty():
    print(q.get(), end=' ')