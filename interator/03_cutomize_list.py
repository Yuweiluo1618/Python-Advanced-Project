#create my own list
class MyList(object):
    def __init__(self):
        self.items = []

    def __iter__(self):
        mi = MyIterator(self.items)
        return mi

    def add_items(self, data):
        self.items.append(data)


class MyIterator(object):
    def __init__(self, items):
        self.items = items
        self.cur_index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.cur_index < len(self.items):
            value = self.items[self.cur_index]
            self.cur_index += 1
            return value
        else:
            raise StopIteration




if __name__ == '__main__':

    mylist = MyList()
    mylist.add_items(1)
    mylist.add_items(2)
    mylist.add_items(3)

    #for value in mylist:

        #print(value)
    mi = iter(mylist)
    print(next(mi))
    print(next(mi))
    print(next(mi))
    print(next(mi))