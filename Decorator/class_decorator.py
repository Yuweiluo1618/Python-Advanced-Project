class Test(object):
    def __init__(self, func):
        print("__init__")
        self.func = func

    def __call__(self, *args, **kwargs):
        print("call")
        self.func()

@Test
def login():
    print("login")


login()


