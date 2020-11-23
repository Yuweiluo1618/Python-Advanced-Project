from gevent import monkey
monkey.patch_all()

import time
import gevent

def work1():
    while True:
        time.sleep(0.5)
        print('work1', gevent.getcurrent())



def work2():
    while True:
        gevent.sleep(0.5)
        print('work2',  gevent.getcurrent())



if __name__ == '__main__':
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    g1.join()
    g2.join()