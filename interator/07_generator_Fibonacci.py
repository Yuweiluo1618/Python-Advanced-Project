def fibonacci(n):
    a = 1
    b = 1

    cur_index = 0
    while True:
        if cur_index < n:
            value = a
            a, b = b, a+b
            cur_index += 1
            yield  value
        else:
            break






f1 = fibonacci(1)
print(next(f1))
print(next(f1))
print(next(f1))