class Goods(object):
    color = "white"
    def __init__(self):
        self.name = "Jack"
        self.age = 16

    def __call__(self, *args, **kwargs):
        print("-------call---------")

    def __str__(self):
        return "This is Goods object"

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        print("--del--")

if __name__ == '__main__':

    goods = Goods()
    goods()
    print(goods.__dict__)
    print(Goods.__dict__)
    print(goods)

    goods['a']
    del goods['a']