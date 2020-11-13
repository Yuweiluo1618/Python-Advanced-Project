import threading
import time

def A():
    for i in range(2):
        print(threading.current_thread())
        print('A')
        time.sleep(0.5)


def B():
    for i in range(2):
        print(threading.current_thread())
        print('B')
        time.sleep(0.5)


if __name__ == '__main__':

    A_th = threading.Thread(target=A)
    B_th = threading.Thread(target=B)

    A_th.start()
    B_th.start()

    while True:
        print(threading.current_thread())
        th_list = len(threading.enumerate())
        if th_list == 1:
            break
        time.sleep(0.5)

