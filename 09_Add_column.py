import Function as fl
import pymysql

con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
curs=con.cursor()
print('Cloud Database connected successfully')
print('*'*40)
print('Programming is about to add column into table if column find duplicate then to delete or modify column and To Display column list also')
print('*'*40)
input1=input('Enter Column name to add into Mobile Table: ')
print('*'*40)
curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'MOBILES'")
Data=curs.fetchall()
mylist = []
for tuple in Data:
    mylist = mylist + list(tuple)
(mylist)
li=mylist
l=[x.lower() for x in mylist]
if input1.isalpha()==True:
    if input1.lower() not in l:
        input2=input('what type of data you want added column int/float/str: ')
        if input2!='int'or'float'or'str':
            if input2.lower()=='int':
                curs.execute("ALTER TABLE MOBILES ADD %s int" %input1)
                print('*'*40)
                print('Column added successfully')
                x=fl.More_1(input1)
                print(x)
            elif input2.lower()=='float':
                curs.execute("ALTER TABLE MOBILES ADD %s float" %input1)
                print('*'*40)
                print('Column added successfully')
                x=fl.More_1(input1)
                print(x)
                
            elif input2.lower()=='str':
                try:
                    input3=int(input('Enter length of character in nunbers i.e. 1,2,,,50: '))
                    curs.execute("ALTER TABLE MOBILES ADD %s varchar(%d)" %(input1,input3))
                    print('*'*40)
                    print('Column added successfully') 
                    x=fl.More_1(input1)
                    print(x)
                except:
                    print('*'*40)
                    print('Enter valid number')
                                
            else:
                print('*'*40)
                print('Please Enter valid input')   
        
        else:
            print('Please Enter valid input')
    else:
            print('Mobile data found duplicate')
            print('*'*40)
            x=fl.More_2(input1,li)
            print(x) 
else:
    print('Enter Column name in alphabet without space')
con.close()