import os
import multiprocessing
import time

def copy_work(src_dir, dest_dir, file_name):
    print(multiprocessing.current_process)
    src_path = src_dir+'/'+file_name
    dest_path = dest_dir+'/'+file_name
    with open(src_path, 'rb') as src_file:
        with open(dest_path, 'wb') as dest_file:
            while True:
                file_content = src_file.read(1024)
                if not file_content:
                    break
                dest_file.write(file_content)
                time.sleep(0.5)

if __name__ == '__main__':
    src_dir = './copy_src'
    dest_dir = './copy_dst'

    try:
        os.mkdir(dest_dir)

    except:

        print("dir is existed")

    file_name_list = os.listdir(src_dir)
    pool = multiprocessing.Pool(3)

    for file_name in file_name_list:
        #pool.apply(copy_work, (src_dir, dest_dir, file_name))
        pool.apply_async(copy_work, (src_dir, dest_dir, file_name))

    pool.close()

    pool.join()

