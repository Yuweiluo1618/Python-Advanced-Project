import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', database='jing_dong')
cur = conn.cursor()
sql = "select * from goods where name = %s"
params = ['bag1']
ret = cur.execute(sql, params)
print(ret)
print(cur.fetchall())

cur.close()
conn.close()
