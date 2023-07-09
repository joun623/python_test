import model_v7 as model

#@model.entity
class LineItem(model.Entity):
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

LineItem("hoge", 200, 500)
LineItem("hoge", 0, 500)
