import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
print('Cloud Database connected successfully')

curs.execute("select RAM from MOBILES")
data=curs.fetchall()
mylist = []
for tuple in data:
    mylist = mylist + list(tuple)
print('Below are the RAM you can select')
mylist = list(dict.fromkeys(mylist))
print(mylist)

curs.execute("select ROM from MOBILES")
Data=curs.fetchall()
Mylist = []
for tuple in Data:
    Mylist = Mylist + list(tuple)
print('Below are the ROM you can select')
Mylist = list(dict.fromkeys(Mylist))
print(Mylist)

input1=int(input('What RAM you want to filter (GB): '))  
input2=int(input('What Rom you want to filter (GB): ')) 
print('*'*40)



curs.execute("select modelnm from MOBILES WHERE RAM='%d' and ROM='%d'"%(input1,input2))
Data=curs.fetchall()
mylist = []
for tuple in Data:
    mylist = mylist + list(tuple)
print('shown models having ram: %d rom: %d'%(input1,input2))
print(mylist)
 
con.close()