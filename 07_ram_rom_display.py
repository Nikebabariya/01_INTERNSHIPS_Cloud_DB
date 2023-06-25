import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
print('Cloud Database connected successfully')
curs.execute("select modelnm, RAM, ROM from MOBILES ")
Data=curs.fetchall()
print('shown data is about ram rom details of mobile model')
print('*'*40)
print(Data)
con.close()
