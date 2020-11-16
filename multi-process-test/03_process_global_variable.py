import multiprocessing
import time

#process will deep copy global variable cannot share it unlike threading
data_list=[1,[1.2],3,4,5]

def A():
    global  data_list
    for i in range(5):
        data_list[1].append(1)
    print("A", data_list)

def B():
    time.sleep(3)
    print("B", data_list)


if __name__ == '__main__':
    a_pro = multiprocessing.Process(target=A)
    b_prp = multiprocessing.Process(target=B)

    a_pro.start()
    b_prp.start()


    time.sleep(5)
    print("main", data_list)