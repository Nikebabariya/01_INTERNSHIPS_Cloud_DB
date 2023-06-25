import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
Compnm=input('Enter a mobile comapany to search model from data: ')
curs.execute("select * from MOBILES where company='%s' order by price"%Compnm)
Data=curs.fetchall()

if  Data:
    print(Data)
else:
    print('Searched mobile data not found')
con.close()