def fibonacci(n):
    a = 1
    b = 1
    cur_index = 0

    while cur_index < n:
        value = a
        a, b = b, a+b
        cur_index += 1
        c = yield a

        if c == 1:
            return 'stop the generator'


fib = fibonacci(2)

print(next(fib))
try:
    print(fib.send(2))

except Exception as e:
    print(e)