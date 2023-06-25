import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
curs.execute("select prodid from MOBILES")
data=curs.fetchall()
mylist = []
for tuple in data:
    mylist = mylist + list(tuple)
print(mylist)
for i in range(len(mylist)):
    curs.execute("select prodid, modelnm from MOBILES where prodid=%d"%mylist[i])
    data=curs.fetchone()
    print(data)
    ask=input('Enter Porpose gaming/office/social: ')
    curs.execute("UPDATE MOBILES SET PORPOSE='%s' WHERE prodid=%d"%(ask,mylist[i]))
    con.commit()

curs.execute("select prodid, modelnm, PORPOSE from MOBILES ")
data=curs.fetchall()
print(data)
con.close()