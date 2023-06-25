import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()

print('successfully connected to the cloud database')
cho='yes'
while cho.lower()=='yes':

    prodid=int(input('Enter product id: '))
    Mdlnm=input('Enter Model name: ')
    Compnm=input('Enter company name: ')
    Conn=input('Enter Network connectivity 4G/5G: ')
    ram=int(input('Enter ram (GB): '))
    rom=int(input('Enter rom (GB): '))
    Clr=input('Enter Mobile colour: ')
    Scr=float(input('Enter screen (inch): '))
    Dis=input('Enter type of Display: ')
    Batt=int(input('Enter Battery (mAh): '))
    Proc=input('Enter processor (cores): ')
    Opsy=input('Enter operating system: ')
    prc=float(input('Enter Mobile price: '))
    rat=float(input('Enter mobiles ratings (out of 5): '))
    cho=input('Do you Want to add more mobile data yes/no: ')

    curs.execute("insert into MOBILES values(%d,'%s','%s','%s',%d,%d,'%s',%.2f,'%s',%d,'%s','%s',%.2f,%.2f)" %(prodid,Mdlnm,Compnm,Conn,ram,rom,Clr,Scr,Dis,Batt,Proc,Opsy,prc,rat))
    con.commit()
    print('Mobile data added successfully')

con.close()