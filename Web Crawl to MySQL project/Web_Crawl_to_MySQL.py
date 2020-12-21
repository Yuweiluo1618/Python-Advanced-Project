import urllib.request
import re
import pymysql
import threading
import time

def get_movie(links):
    response = urllib.request.urlopen(links)
    response_text = response.read().decode("GBK")
    link_list = re.findall('<a href="(.*)" class="ulink">(.*)</a>', response_text)
    get_down_load_links(link_list)

def get_down_load_links(link_list):
    conn = pymysql.connect(host='localhost', user='root', password='', database='movie_db')
    cur = conn.cursor()
    for link, movie_name in link_list:
        link = 'https://www.ygdy8.net'+ link
        response = urllib.request.urlopen(link)
        response_text = response.read().decode("GBK")
        down_load_link = re.search('<a href="(.*)">ftp:', response_text)
        if down_load_link:
            store_to_database(down_load_link.group(1), movie_name, cur, conn)
            #print(down_load_link.group(1))
        else:
            print("match fail")
    cur.close()
    conn.close()

def store_to_database(movie_link, movie_name, cur, conn):

    params = [movie_name, movie_link]
    if exist_database(movie_name, cur):
        print("1")
        cur.execute('insert into movie_link values(null, %s, %s)', params)
        conn.commit()

    else:
        print("movie has existed")


def exist_database(movie_name, cur):
    params = [movie_name]
    ret = cur.execute("select * from movie_link where film_name = %s", params)
    if ret:
        return False
    return True

def main():
    links = 'https://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
    get_movie(links)



if __name__ == '__main__':
    main()


