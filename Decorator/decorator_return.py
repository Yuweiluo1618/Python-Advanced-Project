def function_out(func):
    def function_in():
        print("function_in")
        return func()
    return function_in

@function_out
def function_ori():
    print('ori')
    return 10

print(function_ori())