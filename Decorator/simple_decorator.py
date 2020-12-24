def function_out(func):
    def function_in():
        print('new feature')
        func()
    return function_in

@function_out
def function_ori():
    print('old feature')

#res = function_out(function_ori)
#res()

function_ori()