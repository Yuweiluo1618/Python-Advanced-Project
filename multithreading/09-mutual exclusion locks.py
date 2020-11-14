import threading
import time

glo_vari = 0

def A():
    global glo_vari

    for i in range(1000000):
        lock1.acquire()
        glo_vari += 1
        lock1.release()

    print('A', glo_vari)

def B():
    global glo_vari

    for i in range(100000):
        lock1.acquire()
        glo_vari += 1
        lock1.release()
    print('B', glo_vari)

if __name__ == '__main__':
    t1 = threading.Thread(target=A)
    t2 = threading.Thread(target=B)
    lock1 = threading.Lock()

    t1.start()
    t2.start()

    if len(threading.enumerate()) != 1:
        time.sleep(0.5)

    print('main', glo_vari)