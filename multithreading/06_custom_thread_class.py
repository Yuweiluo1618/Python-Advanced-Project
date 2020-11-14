import threading
import time

class MyThread(threading.Thread):
    def __init__(self, num):
        super(MyThread, self).__init__()
        self.num = num

    def run(self):
        print(self.num)

        for i in range(1,10):
            print(i)
            print(self.name)
            time.sleep(0.5)

if __name__ == '__main__':
    mythread = MyThread(1)
    mythread.start()
    print(threading.current_thread())