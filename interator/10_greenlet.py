from greenlet import greenlet
import time

def work1():
    while True:
        print('work1')
        time.sleep(0.5)
        g2.switch()


def work2():
    while True:
        print('work2')
        time.sleep(0.5)
        g1.switch()


if __name__ == '__main__':
    g1 = greenlet(work1)
    g2 = greenlet(work2)

    g1.switch()