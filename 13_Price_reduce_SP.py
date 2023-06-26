import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()

print('Cloud Database connected successfully')
print('*'*40)

print('Below are the mobile models with their price')
curs.execute("select modelnm, Price from MOBILES")
data=curs.fetchall()
print(data)
print('*'*40)

curs.execute("call Reduprice")

print('Below are the mobile models price after 3"%" reduction in price')
curs.execute("select modelnm, Price from MOBILES")
Data=curs.fetchall()
print(Data)




print('*'*40)