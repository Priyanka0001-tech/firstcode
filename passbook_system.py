import mysql.connector
import datetime
x=datetime.datetime.now()
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jycfjffx",
    database="atm"
)
cur=con.cursor()
balance=0
cur.execute("use atm;")
query = "INSERT INTO transc (Amount,debit,credit,Datetime)VALUES(%s, %s, %s,%s)"
while(True):
    choice=int(input("Enter \n1 for Deposite \n2 for Widrawal \n3 for Check Balance \nEnter your choice:"))
    if choice==1:
        amount=int(input("Enter the amount to deposite: "))
        balance=balance+amount
        cur.execute(query, (balance,0,amount,x))
    elif choice==2:
        amount=int(input("Enter the amount to withdraw: "))
        if amount>balance:
            print("!!Insufficient balance!!")
        else:
            balance-=amount
            cur.execute(query, (balance,amount,0,x))
            print("Your new balance is:",balance)
    elif choice==3:
        print("Your current balance is:",balance)
    else:
        print("Invalid choice")
    print("Order placed successfully.")
    con.commit()  
con.close()