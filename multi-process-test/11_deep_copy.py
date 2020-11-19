import multiprocessing
import time

list1 = [1,2,3,4,5]

def A():
    global list1
    print(id(list1))
    list1.append(1)

def B(list1):
    print(id(list1))
    list1.append(2)
    print(list1)


if __name__ == '__main__':
   a_process = multiprocessing.Process(target=A)
   b_process = multiprocessing.Process(target=B, args=(list1, ))

   a_process.start()
   a_process.join()
   b_process.start()
   b_process.join()
   time.sleep(3)
   print(id(list1))
   print(list1)
