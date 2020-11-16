import time
import multiprocessing

def A():
    for i in range(10):
        print("A.....")
        time.sleep(0.5)



if __name__ == '__main__':
    pro_obj = multiprocessing.Process(target=A)
    pro_obj.start()