class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

foo = MyObject()
assert foo.public_field == 5

assert foo.get_private_field() == 10

print(foo.__dict__)
print(foo._MyObject__private_field)
