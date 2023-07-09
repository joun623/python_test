import time 
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_generator():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b

n = 10000

start = time.time()
# fibonacci_recursive(n)
for i in fibonacci_generator():
    if i > 10000:
        break
    a = i
print(time.time() - start)



