from collections import Iterator

class A(object):
    pass

class B(object):
    def __iter__(self):
        pass


a = A()
b = B()

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))