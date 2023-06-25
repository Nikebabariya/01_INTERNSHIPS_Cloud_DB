import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
print('Cloud Database connected successfully')
print("Below are the list of available Model's ID")
curs.execute("select prodid from MOBILES")
data=curs.fetchall()
mylist = []
for tuple in data:
    mylist = mylist + list(tuple)
print(mylist)
prod=int(input('Enter a Product ID: '))
curs.execute("select * from MOBILES where prodid='%d'" %prod)
Data=curs.fetchone()
msg=None
if Data:
    print('Mobile Data: ',Data)
    msg=input('Do you want to delete shown mobile data from database yes/no: ')
    if msg=='yes':
        prodid=Data[0]
        curs.execute("delete from MOBILES where prodid=%d" %prodid)
        con.commit()
        print('Mobile Data deleted successfully')
    else:
         print('Data is not deleted')
else:
        print('Mobile model not found')
con.close()
