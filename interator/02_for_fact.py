list1 = [1, 3, 5, 7, 9]
list1_iterator = iter(list1)

while True:
    try:
        value = next(list1_iterator)
        print(value)
    except Exception as e:
        break