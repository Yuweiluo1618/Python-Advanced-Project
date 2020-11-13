import threading
import time
#Set to Deamon thread
def A():
    for i in range(10):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    a_th = threading.Thread(target=A)
    a_th.setDaemon(True)
    a_th.start()

    time.sleep(2)
    print('game over')
    exit()