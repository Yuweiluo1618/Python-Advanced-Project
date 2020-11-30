import urllib.request
import re
import threading
import time

# this is the simplr multi-threads web carwler program can help people gather the movie data
movie_download_list = dict()
lock1 = threading.Lock()

def get_movie_links(links):
    response = urllib.request.urlopen(links)
    response_text = response.read().decode("GBK")
    link_list = re.findall(r'<a href="(.*)" class="ulink">(.*)</a>', response_text)
    for i in link_list:
        get_movie_download_links(i,link_list)



def get_movie_download_links(i, link_list):
    global movie_download_list
    response = urllib.request.urlopen("https://www.ygdy8.net"+i[0])
    response_text = response.read().decode("GBK")
    result = re.search(r'<a href="(.*)">ftp:', response_text)
    if result:
        lock1.acquire()
        movie_download_list[i[1]] = result.group(1)
        lock1.release()
    else:
        print("match fail")



def main():
    for i in range(1,5):
        links = "https://www.ygdy8.net/html/gndy/dyzz/list_23_"+str(i)+".html"
        i += 1
        #get_movie_links(links)
        download_thread = threading.Thread(target=get_movie_links, args=(links, ))
        download_thread.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)
    for movie_name, download_link in movie_download_list.items():
        print(f"{movie_name} : {download_link}")

if __name__ == '__main__':
    main()