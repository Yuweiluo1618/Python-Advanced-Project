import time
import threading

#Comparing
def saysomething():
    print("hi")
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        saysomething()

    print('--------------------------')

    for i in range(5):
        obj_th = threading.Thread(target=saysomething)
        obj_th.start()