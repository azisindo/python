from __future__ import print_function
import cx_Oracle

conn=cx_Oracle.connect('test/test@10.231.12.220:1094/ITDEV9I')
ver = conn.version.split(".")
print(ver)

cur=conn.cursor()
cur.execute('select * from unit_usaha')
for result in cur:
    print(result)
cur.close()
conn.close()







