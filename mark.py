import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marksheet"
)
n=int(input("1.insert 2.delete 3.select 4.update 5.search"))
if(n==1):
    print("insert values")
    sno=int(input("enter student no"))
    sname=input("enter student name")
    tamil=int(input("enter tamil mark"))
    eng=int(input("enter english mark"))
    maths=int(input("enter maths mark"))
    science=int(input("enter science mark"))
    social=int(input("enter social mark"))
    tot=tamil+eng+maths+science+social
    avg=tot/5
    mycursor=mydb.cursor()
    sql="insert into mark(sno,sname,tamil,eng,maths,science,social,tot,avg)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(sno,sname,tamil,eng,maths,science,social,tot,avg)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")
elif(n==2):
    print("record delete")
    sno = int(input("enter student no"))
    mycursor = mydb.cursor()
    sql="delete from mark where sno={}".format(sno)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,"record deleted")
elif(n==3):
    print("select all the records")
    mycursor = mydb.cursor()
    mycursor.execute("select * from mark order by sname")
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)
elif(n==4):
    print("record updated")
    sno = int(input("enter student no"))
    sname = input("enter student name")
    mycursor = mydb.cursor()
    sql="update mark set sname=%s where sno=%s"
    val=(sno,sname)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record updated")
elif(n==5):
    print("search record")
    mycursor=mydb.cursor()
    sql="select * from mark where sname like's%'"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    print(myresult,"record searched")
else:
    print("record not available")
