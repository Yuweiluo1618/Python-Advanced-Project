import multiprocessing
import time

queue1 = multiprocessing.Queue(2)
queue1.put(1)
queue1.put(2)

#add time.sleep() or will cause bug
time.sleep(0.0005)
print(queue1.full())
print(queue1.qsize())
print(queue1.empty())
