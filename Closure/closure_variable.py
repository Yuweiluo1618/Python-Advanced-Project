def outter(num):
    def inner():
        nonlocal num
        print(num)
        num = 99
    return inner

ret = outter(10)
ret()