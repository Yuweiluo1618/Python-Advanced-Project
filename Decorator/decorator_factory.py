def factory(path):
    def function_out(func):
        print(path)
        def function_in():
            print('new features')
            func()
        return  function_in
    return function_out

@factory("login.py")
def login():
    print("login")


@factory("register.py")
def resigter():
    print("register")

login()
resigter()