
class Item:
  all = []
  def __init__(self, name: str, price: float, quantity:int ):
    #Assert. Validating the data. Make sure the price or quantity is not negative
    assert price >= 0, f"Price {price} should be positive"
    assert quantity >= 0, AssertionError("Quantity {quantity} should be positive")
    
    #Assigning self to the attributes
    self.name = name
    self.price = price
    self.quantity = quantity

    Item.all.append(self)

  def __repr__(self):
    return f"Item('{self.name}, {self.price}, {self.quantity}')"
               

  def total_price(self):
    return self.price * self.quantity
  
item1 = Item("Phone", 600, 5)
item2 = Item('Laptop', 1400, 3)
print(item1.quantity)
print(item2.total_price())
# print(Item.__dict__)
print(item1.__dict__)

for instance in Item.all:
  print(instance.name)

print(Item.all)
