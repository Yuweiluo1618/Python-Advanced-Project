class Page(object):
    def __init__(self, num):
        self.num = num

    @property
    def prop(self):
        return  self.num


page =  Page(3)
print(page.num)