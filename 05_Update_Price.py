import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
print('Cloud Database connected successfully')
print('please enter Product id number out of below list')
print('*'*40)
con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
curs.execute("select prodid from MOBILES")
data=curs.fetchall()
mylist = []
for tuple in data:
        mylist = mylist + list(tuple)
print(mylist)
try:
        prodid=int(input('Enter a product Id: '))
        curs.execute("select * from MOBILES where prodid=%d" %prodid)
        Data=curs.fetchone()
        data=Data[0]
        print('Mobile current price: ',Data[14])
        pr=float(input('Enter new price : '))
        curs.execute("update MOBILES set price=%.2f where prodid=%d" %(pr,prodid))
        con.commit()
        print('Price updated successfully')
except:
        print('Mobile data not found, please enter valid input')
con.close()
