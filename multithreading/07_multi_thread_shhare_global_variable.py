import threading
import time

glo_v = 0

def A():
    global glo_v
    for i in range(10000000):
        glo_v += 1

    print(glo_v)

def B():
    print('B', glo_v)


if __name__ == '__main__':
    t1 = threading.Thread(target=A)
    t2 = threading.Thread(target=B)

    t1.start()
    t2.start()


    if len(threading.enumerate()) != 1:
        time.sleep(1)
    print(glo_v)