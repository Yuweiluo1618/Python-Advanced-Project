class Goods(object):
    def __init__(self):
        self.org_price = 1000
        self.discount = 0.7

    def get_price(self):
        return self.org_price*self.discount

    def set_price(self, val):
        self.org_price = val

    def del_price(self):
        print("delete price")

    BAR = property(get_price, set_price, del_price, "this is price class")

if __name__ == '__main__':
    goods = Goods()
    print(goods.BAR)
    goods.BAR = 500
    print(goods.BAR)
    del goods.BAR
    print(Goods.BAR.__doc__)
