def function_out(func):
    def function_in(num):
        print('func_in ', num)
        func(num)
    return function_in

def function_out2(func):
    def function_in2(*args, **kwargs):
        print('func_in2 args: ', args)
        print('func_ori2 kwargs:', kwargs)
        func(*args, **kwargs)
    return function_in2

@function_out
def function_ori(num):
    print('ori ',num)

#function_ori(3)

@ function_out2
def function_ori2(*args, **kwargs):
    print('ori2: args: ', args)
    print('ori2 kwargs: ', kwargs)

function_ori2(1, a=3)