def outter(num_out):
    print("out", num_out)
    def inner(num_in):
        print('in', num_out)
        print('in', num_in)

    return  inner


a = outter(3)
a(4)
