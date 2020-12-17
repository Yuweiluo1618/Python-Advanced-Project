import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', database='jing_dong')
cur = conn.cursor()
#sql = "insert into goods values(null, 'bag3', 1, 8, 66, 1, 0)"
sql1 = 'update goods set price = 68 where id = 22'
ret = cur.execute(sql1)
conn.commit()
print(ret)
cur.close()
conn.close()