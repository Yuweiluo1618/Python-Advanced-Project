def test1(*args, **kwargs):
    print(args)
    print(kwargs)
    test2(*args, **kwargs)

def test2(*args, **kwargs):
    print("-----test2------")
    print(args)
    print(kwargs)


if __name__ == '__main__':
    test1(1,2,3,4,5,a=10,b=20)
