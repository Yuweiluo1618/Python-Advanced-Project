import threading
import time

glo_v = 0

def A():
    global  glo_v
    for i in range(1000000):
        glo_v += 1

    print("A", glo_v)

def B():
    global glo_v
    for i in range(10000000):
        glo_v += 1
    print('B', glo_v)

if __name__ == '__main__':
    t1 = threading.Thread(target=A)
    t2 = threading.Thread(target=B)
    t1.start()
    t1.join()
    t2.start()

    if len(threading.enumerate()) != 1:
        time.sleep(1)

    print('main', glo_v)