import multiprocessing
import time

def A():
    print("A....")
    time.sleep(0.5)

if __name__ == '__main__':
    pool = multiprocessing.Pool(3)

    for i in range(10):
        #pool.apply(A)
        pool.apply_async(A)


    pool.close()
    pool.join()
