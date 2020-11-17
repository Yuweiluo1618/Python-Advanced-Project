import multiprocessing

def A(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    a_process = multiprocessing.Process(target=A, args=(10, ), kwargs={'c': 1000, 'b': 100})
    a_process.start()
