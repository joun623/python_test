import model_v5 as model

@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

def entity(cls):
    for key, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            type_namae = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name, key)
    return cls

LineItem("hoge", 200, 500)
LineItem("hoge", 0, 500)
