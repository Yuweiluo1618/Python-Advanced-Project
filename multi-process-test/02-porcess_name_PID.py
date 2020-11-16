import time
import multiprocessing
import os

def A():
    for i in range(10):
        print('A', multiprocessing.current_process(), multiprocessing.current_process().pid)
        print(os.getpid(), os.getppid())
        time.sleep(1)

if __name__ == '__main__':
    print(multiprocessing.current_process(), os.getpid(), os.getppid())
    pros_obj = multiprocessing.Process(target=A, name='p1')
    pros_obj.start()