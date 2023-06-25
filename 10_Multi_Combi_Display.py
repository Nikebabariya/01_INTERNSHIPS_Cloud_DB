import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
print('Cloud Database connected successfully')
print('*'*20)
print('Mobile Data list')
curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'MOBILES'")
Data=curs.fetchall()
#for index, tub in enumerate(Data):
#    print(tub[0])
myList = []
for tuple in Data:
   myList = myList + list(tuple)
print(myList)
print('*'*20)
print('1. To Display Two specification from above shown list')
print('2. To Display Three specification from above shown list')
print('3. To Display Four specification from above shown list')
print('4. To Display Five specification from above shown list')
print('5. Exit from query')
try:
    cho=int(input('Enter your choice (1/2/3/4/5) : '))
    if cho==1:
        Input1=input('Enter type of mobile data from above list: ')
        Input2=input('Enter type of mobile data from above list: ')
        curs.execute("select %s, %s from MOBILES" %(Input1,Input2))
        data=curs.fetchall()
        print(data)
    elif cho==2:
        Input1=input('Enter type of mobile data from above list: ')
        Input2=input('Enter type of mobile data from above list: ')
        Input3=input('Enter type of mobile data from above list: ')
        curs.execute("select %s, %s, %s from MOBILES" %(Input1,Input2,Input3))
        data=curs.fetchall()
        print(data)
    elif cho==3:
        Input1=input('Enter type of mobile data from above list: ')
        Input2=input('Enter type of mobile data from above list: ')
        Input3=input('Enter type of mobile data from above list: ')
        Input4=input('Enter type of mobile data from above list: ')
        curs.execute("select %s, %s, %s, %s from MOBILES" %(Input1,Input2,Input3,Input4))
        data=curs.fetchall()
        print(data)
    elif cho==4:
        Input1=input('Enter type of mobile data from above list: ')
        Input2=input('Enter type of mobile data from above list: ')
        Input3=input('Enter type of mobile data from above list: ')
        Input4=input('Enter type of mobile data from above list: ')
        Input5=input('Enter type of mobile data from above list: ')
        curs.execute("select %s, %s, %s, %s, %s from MOBILES" %(Input1,Input2,Input3,Input4,Input5))
        data=curs.fetchall()
        print(data)
    elif cho==5:
        print('Thanks for visit')
    else:
        print('Data is not found')
except:
    print('Please enter valid input')

con.close()
