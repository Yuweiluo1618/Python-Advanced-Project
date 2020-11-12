import threading
import time


def sing():
    for i in range(5):
        print("singing...")
        time.sleep(1)


def dance():
    for i in range(5):
        print('dancing........')
        time.sleep(1)


if __name__ == '__main__':
    sing_th = threading.Thread(target=sing)
    dance_th = threading.Thread(target=dance)
    sing_th.start()
    dance_th.start()