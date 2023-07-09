def deco(func):
    def inner():
        print('runninng inner')
    return inner

def odeco(func):
    print('running inner')

    return func

@odeco
def target():
    print('running target()')

target()
print(target)
