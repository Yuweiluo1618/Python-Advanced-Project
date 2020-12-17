import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', database='jing_dong')
cur = conn.cursor()
sql = "insert into goods values(null, 'bag3', 1, 8, 66, 1, 0)"
ret = cur.execute(sql)
conn.commit()
print(ret)
cur.close()
conn.close()