import multiprocessing
import time

def send_queue(queue):
    #while not queue.full():
    while True:
        queue.put(1)
        queue.put(2)
        time.sleep(0.5)
        queue.put(3)

def recv_queue(queue):
    while queue.qsize != 0:
        print(queue.get())


if __name__ == '__main__':
    queue1 = multiprocessing.Queue(3)

    send_process = multiprocessing.Process(target=send_queue, args=(queue1, ))
    recv_process = multiprocessing.Process(target=recv_queue, args=(queue1, ))

    send_process.start()
    time.sleep(0.5)
    recv_process.start()