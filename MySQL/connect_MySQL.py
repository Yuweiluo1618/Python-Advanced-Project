import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', database='jing_dong')
cur = conn.cursor()
result = cur.execute("select * from goods")
#print(result)
#result_list = cur.fetchone()
result_list = cur.fetchall()
for i in result_list:
    print(i)
cur.close()
conn.close()