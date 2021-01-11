class Goods(object):
    def __init__(self):
        self.org_price = 700
        self.discount = 0.7

    @property
    def price(self):
        return self.org_price * self.discount

    @price.setter
    def price(self, val):
        self.org_price = val

    @price.deleter
    def price(self):
        print("delete price")


goods = Goods()
print(goods.price)
goods.price = 300
print(goods.price)
del goods.price