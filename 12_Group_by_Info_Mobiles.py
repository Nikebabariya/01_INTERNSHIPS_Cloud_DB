import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
print('Cloud Database connected successfully')
print('*'*40)
print('this program about to display group by information - brand, total models under the company, average price, average rating and ROM. ROM Taken as field and displayed all mobiles in the descending order of ROM.')
print('*'*40)
curs.execute("select company, count(modelnm), avg(Rating), avg(Price), ROM from MOBILES group by company order by ROM desc")
data=curs.fetchall()
print(data)
con.close()