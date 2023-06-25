import pymysql

def More_1(input1):
    con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
    curs=con.cursor()
    cho=input('Do you want column in table yes/no: ')
    if cho.lower()=='yes':
        print('*'*40)
        print('newly added column saved')
        
    else:
        
        curs.execute("ALTER TABLE MOBILES Drop COLUMN %s" %input1)
        print('*'*40)
        print('column deleted successfully')

    curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'MOBILES'")
    Data=curs.fetchall()
    mylist = []
    for tuple in Data:
        mylist = mylist + list(tuple)
    return(mylist)

def More_2(input1,li):
    con=pymysql.connect(host='bkjttnootiu2k1ix6olk-mysql.services.clever-cloud.com',user='uqhiaxc1ndrl6yqq',password='viE6QcaH6BiHCUYHasXU',database='bkjttnootiu2k1ix6olk')
    curs=con.cursor()
    if input1 in li:
        cho=input('Do you want column in table yes/no: ')
        if cho.lower()=='yes': 
            ask=input('Do you want to modify column? yes/no: ')
            if ask.lower()=='yes':
                Do=input('What do you want column Rename/Modify/Both?: ')
                if Do.lower()=='rename':
                    renam=input('Enter new name for column: ') 
                    curs.execute("ALTER TABLE MOBILES RENAME COLUMN %s to %s"%(input1,renam))
                    print('*'*40)
                    print('Column name modified successfully')
                    print('*'*40)

                elif Do.lower()=='modify':
                    Mody=input('Enter data type for column int/float/str: ')
                    if Mody.lower()!='int'or'float'or'str':
                        if Mody.lower()=='int':
                            curs.execute("ALTER TABLE MOBILES MODIFY COLUMN %s %s" %(input1,Mody))
                            print('*'*40)
                            print('column Modify successfully')
                        elif Mody.lower()=='float':
                            curs.execute("ALTER TABLE MOBILES MODIFY COLUMN %s %s" %(input1,Mody))
                            print('*'*40)
                            print('column Modify successfully')
                        elif Mody.lower()=='str':
                            try:
                                Num=int(input('Enter length of character in nunbers i.e. 1,2,,,50: '))
                                curs.execute("ALTER TABLE MOBILES MODIFY COLUMN %s varchar(%d)" %(input1,Num))
                                print('*'*40)
                                print('Column modify successfully')
                            except:
                                print('*'*40)
                                print('enter valid number')

                elif Do.lower()=='both':
                    renam=input('Enter new Column name: ') 
                    curs.execute("ALTER TABLE MOBILES RENAME COLUMN %s to %s"%(input1,renam))
                    print('*'*40)
                    print('Column name modified successfully')
                    print('*'*40)
                    Mody=input('Enter data type for column int/float/str: ')
                    if Mody!='int'or'float'or'str':
                        if Mody.lower()=='int':
                            curs.execute("ALTER TABLE MOBILES MODIFY COLUMN %s %s" %(renam,Mody))
                            print('*'*40)
                            print('column Modify successfully')
                        elif Mody.lower()=='float':
                            curs.execute("ALTER TABLE MOBILES MODIFY COLUMN %s %s" %(renam,Mody))
                            print('*'*40)
                            print('column Modify successfully')
                        elif Mody.lower()=='str':
                            try:
                                Num=int(input('Enter length of character in nunbers i.e. 1,2,,,50: '))
                                curs.execute("ALTER TABLE MOBILES MODIFY COLUMN %s varchar(%d)" %(renam,Num))
                                print('*'*40)
                                print('Column modify successfully')
                            except:
                                print('*'*40)
                                print('enter valid number') 
                else:
                    print('Enter valid input')
                
            curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'MOBILES'")
            Data=curs.fetchall()
            mylist = []
            for tuple in Data:
                mylist = mylist + list(tuple)
            return(mylist)
        else:
            curs.execute("ALTER TABLE MOBILES Drop COLUMN %s" %input1)
            print('*'*40)
            print('column deleted successfully')
            curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'MOBILES'")
            Data=curs.fetchall()
            mylist = []
            for tuple in Data:
                mylist = mylist + list(tuple)
            return(mylist)    
    else:
        print('Entered column name: ',input1)
        print('*'*40)
        print('Please check entered column name in below list may be it is look like "same=SAME"')
        print('*'*40)
        curs.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'MOBILES'")
        Data=curs.fetchall()
        mylist = []
        for tuple in Data:
            mylist = mylist + list(tuple)
        return(mylist)




    
