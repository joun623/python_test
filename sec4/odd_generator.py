def odd_generator():
    for i in range(10):
        if i % 2 == 1: 
            yield i

print(odd_generator())
