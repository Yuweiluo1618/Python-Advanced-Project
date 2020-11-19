import os
import multiprocessing
import time

def file_copy(file_name):
    print(multiprocessing.current_process)
    with open('./copy_src/'+file_name, 'rb') as file_read:
        while True:
            read_content = file_read.read(1024)
            if not read_content:
                break
            with open('./copy_dst/'+file_name, 'wb') as file_copy:
                file_copy.write(read_content)
                time.sleep(0.5)




if __name__ == '__main__':
    file_list = os.listdir('./copy_src')
    pool = multiprocessing.Pool(3)
    for file_name in file_list:
        pool.apply_async(file_copy,(file_name, ))

    pool.close()
    pool.join()