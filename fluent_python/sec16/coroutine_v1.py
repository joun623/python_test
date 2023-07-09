def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
