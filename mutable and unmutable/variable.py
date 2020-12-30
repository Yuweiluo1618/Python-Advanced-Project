def mutable():
    a = 1
    print("a:", id(a))
    a += 1
    print("a:",id(a))

def unmutable():
    a = [1]
    print("a:", id(a))
    a.append(3)
    print("a:", id(a))
    b = a
    b.append(5)
    print("b:", id(b))

unmutable()