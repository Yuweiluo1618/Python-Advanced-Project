import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', database='python_index_db')
cur = conn.cursor()
for i in range(100000):
    sql = f"insert into test_index(title) values('ha-{str(i)}')"
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()