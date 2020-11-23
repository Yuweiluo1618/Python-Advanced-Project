import  time

def work1():
    while True:
        print('work1')
        yield
        time.sleep(1)


def work2():
    while True:
        print('work2')
        yield
        time.sleep(1)


if __name__ == '__main__':
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)