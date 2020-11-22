list_data = [ value for value in range(10)]
print(list_data)


#generator

generator1 = (value for value in range(10))
print(next(generator1), '->')
for value in generator1:
    print(value)


def generator2():
    yield 100


print(next(generator2()))
print(next(generator2()))