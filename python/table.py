import mysql.connector
class Cust_info:
    cust_name=""
    bill_amt=0
    def data_entry(self):
        self.cust_name=input("enter the name")
        self.bill_amt=input("Enter the bill amount")
        conn = mysql.connector.connect(host = "localhost", user="root",password="", database="customer")
        c  = conn.cursor()
        sql = "insert into bill_details values('" + self.cust_name + "','" + self.bill_amt +"')"
        c.execute(sql)
        conn.commit()
        print("Record addeddd.")
    def display(self):
        conn = mysql.connector.connect(host = "localhost", user="root",password="", database="customer")
        c  = conn.cursor()
        sql = "select * from bill_details where bill_amt=(select max(bill_amt) from bill_details)"
        c.execute(sql)
        data = c.fetchall()
        print(data)

 
mylist=[]
print("Enter the number of customers")
n=int(input())
for i in range(n):
    mylist.append(Cust_info())
for obj in mylist:
    obj.data_entry()
obj.display()        