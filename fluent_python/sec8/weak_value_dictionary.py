import weakref

class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog: 
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

del catalog
sorted(stock.keys())

del cheese
sorted(stock.keys())


