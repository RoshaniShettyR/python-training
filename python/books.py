import mysql.connector
import datetime
class Library:
    conn  = mysql.connector.connect(host = "localhost", user="root",password="", database="mydata")
    bnum = 0
    title = ""
    studid=0
    studname=""
    idate = ""
    rdate = ""
    def addbook(self):
        self.bnum = input("Enter book number")
        self.title= input("Title of the book")
        c  = self.conn.cursor()
        c.execute("insert into books values('"+self.bnum+"','"+ self.title +"')")
        self.conn.commit()
    def addstud(self):
        self.studid = input("Enter stud id")
        self.studname  = input("Name of stud")
        c = self.conn.cursor()
        c.execute("insert into student values('"+self.studid+"','"+ self.studname +"')")
        self.conn.commit()
    def issuebook(self):
        book  = input("Enter book to issue")
        stud  = input("Enter studname")
        c  =  self.conn.cursor()
        c.execute("Select * from books where title='"+ book + "'")
        data = c.fetchall()
        if c.rowcount == 0:
            print("Invalid book title")
        else:
            print("...issue in progress...")
            today  =  datetime.datetime.now()
            today  = today.strftime("%d"+"-"+"%m" + "-" + "%Y")            
            c = self.conn.cursor()
            c.execute("insert into issuerecs values('"+book+"','"+ stud +"','" + today  + "','"+ today +"', 0)")    
            self.conn.commit()

    def retbook(self):
        c = self.conn.cursor()
        book  = input("Enter book to issue")
        c.execute("select idate from issuerecs where title='"  + book +"'")
        data  = c.fetchall()
        idate  = data[0]
        #fetched the issue date
        print(idate)
        #the rerturn date is he actual date of return hense not calculated here
        rdate  = "25-02-2000"
        #taken fees as default
        fn = 50
        c.execute("update issuerecs set rdate = '"  + rdate + "' where title  = '" +  book +"'")   
        c.execute("update issuerecs set fine = "  + str(fn) + " where title  = '" +  book +"'")   
        self.conn.commit()

obj  = Library()
obj.retbook()