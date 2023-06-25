import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()

curs.execute("create table MOBILES(prodid int primary key,modelnm varchar(20),company varchar(10) not null, Connectivity varchar(3), RAM int, ROM int, color varchar(10), screen float, Display varchar(10), Battery int, Processor varchar(10), Op_system varchar(10), price float not null, rating float);")

print('Mobile Table created successfully')
con.close()