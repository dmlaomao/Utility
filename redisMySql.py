import redis
import MySQLdb
import re
import json
import datetime

r = redis.Redis(host = '...', port = , db = )
conn = MySQLdb.connect(
    host = '',
    port = ,
    user = '',
    passwd = '',
    db = '',
    )
cur = conn.cursor()

def save_mysql(key, typ):
    value = json.loads(r.get(key))
    sysId = value['']['']
    for (d, x) in value.items():
        for (y, z) in x.items():
            sql = 'select id from table where client = '+ typ + ' and name = \'' + y + '\''
            cur.execute(sql)
            idNum = cur.fetchone()
            if idNum:
                sql_insert = 'insert into () values ('+ str(idNum[0]) + ',\'' + z + '\',' + sysId + ', ' + ')'
                try:
                    cur.execute(sql_insert)
                    conn.commit()
                except MySQLdb.Error,e:
                    print 'Mysql Error'
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

keys = r.keys()
for key in keys:
    if re.search('', key):
        save_mysql(key, '0')
    if re.search('', key):
        save_mysql(key,'2')
    if re.search('', key):
        save_mysql(key, '3')

cur.close()
conn.close()
