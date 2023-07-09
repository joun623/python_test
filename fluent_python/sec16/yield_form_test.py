def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i

def gen_from():
    yield from 'AB'
    yield from range(1, 3)

def chain(*iterables):
    for i in iterables:
        yield from i

