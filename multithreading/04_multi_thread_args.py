import threading
import time

def A(a, b ,c):
    print('parameter: ', a, b, c)


if __name__ == '__main__':
    A_th = threading.Thread(target=A, args=(1, ), kwargs={"c": 2, "b": 3})
    A_th.start()


