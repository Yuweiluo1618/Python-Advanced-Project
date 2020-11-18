import multiprocessing
import time

def write_queue(queue):
    for i in range(10):
        if queue.full():
            print('queue is full')
            break
        queue.put(i)
        print('writing to queue...', i)

def read_queue(queue):
    while True:
        if queue.qsize() == 0:
            print('queue is empty')
            break
        value = queue.get()
        print('read from queue', value)

if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    queue = multiprocessing.Manager().Queue(5)

    # syns way
    #pool.apply(write_queue, (queue, ))
    #pool.apply(read_queue, (queue, ))

    #a-syns way
    result = pool.apply_async(write_queue, (queue, ))
    result.wait()
    pool.apply_async(read_queue, (queue, ))

    pool.close()
    pool.join()