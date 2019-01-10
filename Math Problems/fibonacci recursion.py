import time
start_time = time.time()
######################################

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(5):
    print(fibonacci(i),)
#####################################################
end_time = time.time() - start_time
print("##############################################")
print("End Time: ", end_time)
