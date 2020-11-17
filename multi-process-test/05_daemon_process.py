import multiprocessing
import time

def A():
    for i in range(10):
        print('A...')
        time.sleep(1)

def B():
    for i in range(10):
        print('B.....')
        time.sleep(1)

if __name__ == '__main__':
    a_process = multiprocessing.Process(target=A)
    b_process = multiprocessing.Process(target=B)

    a_process.daemon = True

    a_process.start()
    b_process.start()

    time.sleep(2)
    print('main process end')
    b_process.terminate()
    exit()