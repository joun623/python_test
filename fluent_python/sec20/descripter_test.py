def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]

def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

### essential classes for this example ###

class Overriding:
    """a.k.a data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class OverridingNoGet:

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class NonOverriding:

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))

obj = Managed()
#obj.over
#Managed.over
#obj.over = 7
#obj.over
#obj.__dict__['over'] = 8
#vars(obj)
#obj.over

#print(obj.over_no_get)
#print(Managed.over_no_get)
#obj.over_no_get = 7
#print(obj.over_no_get)
#obj.__dict__['over_no_get'] = 8
#print(vars(obj))
#print(obj.over_no_get)

obj.non_over
Managed.non_over
obj.non_over = 7
print(obj.non_over)
Managed.non_over
del obj.non_over
obj.non_over

