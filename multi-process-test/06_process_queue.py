import multiprocessing

if __name__ == '__main__':
    queue1 = multiprocessing.Queue(3)
    queue1.put(1)
    queue1.put(2)
    queue1.put(3)
    #queue1.put_nowait(4)
    print(queue1.get())
    print(queue1.get())
    print(queue1.get())
    #print(queue1.get_nowait())
