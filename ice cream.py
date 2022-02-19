import pandas as pd
import mysql.connector as mydb

mydb=mydb.connect(
  host="localhost",
  user="root",
  password="Ak@1708",
  database="ice_cream"
)

#name of the company
print ("*"*70)
print("\nWelcome to  Natural Ice Creams ")
print("              ~Customized and Provided by  2A- Designers\n")
print ("*"*70)
print("")
lol="yes"
while lol=="yes":

#command to choose what action you need to perform
    print('''\n \n What can I help you with?

    1. Place order
    2. Add a new flavour
    3. Delete an existing flavour
    4. Display all the flavours with prices
    5. Change prices for existing ice cream flavours
    6. Display orders
    7. Exit''')
    
    print("")
    option=int(input("Select your option by entering it's number: "))
    print("")

#command for action 1 i.e. place order
    if option==1:
        check="y"
        
        while check=="y":
            
            fname=input("Enter Customer's Name: ")
            
            fno=int(input("Enter customer's Phone number: ")) 
            print("")
            mycursor=mydb.cursor()
            sq=("INSERT INTO records(custname,custno) VALUES('%s',%s);")%(fname,fno)
            mycursor.execute(sq)
            mydb.commit()
            print("Name of all the flavours: ")
        

            mycursor.execute("SELECT sr_no,flavour from price_table;")
            
        

               

                        
            myresult=mycursor.fetchall()
            for x in myresult:
                print(x)
            count=mycursor.rowcount
            total=0
            check1="yes"
            while check1=="yes":
            
                flavour1=int(input("Enter the number of your choosen flavour: "))
                if flavour1>0 and flavour1<(count+1):
                    mycursor1=mydb.cursor()
                    sql="SELECT * FROM price_table WHERE sr_no=%s"%flavour1
                    mycursor1.execute(sql)
                    myresult=mycursor.fetchall()
                
                    
                    cup=int(input("Enter the quantity of cups you want in these flavour: "))
                    cone=int(input("Enter the quantity of cones you want in these flavour: "))
                    mycursor2=mydb.cursor()
                    sql1="SELECT cup_price FROM price_table WHERE sr_no=%s"%flavour1
                    mycursor1.execute(sql1)
                    myresult=mycursor.fetchone()
                    myresult1=int(myresult[0])
                
                    mycursor2=mydb.cursor()
                    sql2="SELECT cone_price FROM price_table WHERE sr_no=%s"%flavour1
                    mycursor2.execute(sql2)
                    myresult2=mycursor.fetchone()
                    myresult3=int(myresult2[0])

                    total=total+(cup*myresult1)+(cone*myresult3)
                

                    check11=int(input("Do you want to add more items to  bill? (type 1 for yes/any other number for no):"))
                    if check11==1:
                        check1="yes"
                    else:
                        print("\n Total amount to be paid: ₹",total)
                        check1="no"
                        

                else:
                    print("Invalid Number! Please enter your number again.")
                    check1="yes"

                

            else:
                print("")
                check="n"

#command for action 2 i.e. add a new flavour
    elif option==2:
        print("Adding a New flavour")
        fno=(count+1)
        fname= input("Ente name of new flavour")
        fcup=int(input("Enter the price of this flavour in a cup: "))
        fcone=int(input("Enter the price of this flavour in a cone: "))
        mycursor=mydb.cursor()

        sql13="INSERT INTO price_table (sr_no,flavour,cup_price,cone_price) VALUES(%s,'%s',%s,%s)"%(fno,fname,fcup,fcone)
        
        mycursor.execute(sql13)

        mydb.commit()

        print(mycursor.rowcount,"record inserted.")

#command for action 3 i.e. delete a flavour
    elif option==3:
        print("Name of all the flavours:")
        mycursor113=mydb.cursor()
        mycursor113.execute("SELECT sr_no,flavour from price_table")
        myresult113=mycursor113.fetchall()
        for x13 in myresult113:
            print(x13)

        fnumber=int(input("Enter the number of flavour you want to delete"))
        mycursor200=mydb.cursor()
        sql200="DELETE FROM price_table WHERE sr_no=%s"%fnumber
        mycursor200.execute(sql200)
        mydb.commit()
        print(mycursor200.rowcount, "record(s) deleted")

#command for action 4 i.e. display's all the flavours
    elif option==4:
        print ("*"*70)
        print("Displaying all the flavours with prices:\n")
        mycursor1123=mydb.cursor()
        mycursor1123.execute("SELECT * from price_table")
        myresult1123=mycursor1123.fetchall()
        for x123 in myresult1123:
            print(x123)

#command for action 5 i.e. change price of a flavour 
    elif option==5:
        print("Displaying all the flavours with prices: ")
        mycursor11213=mydb.cursor()
        mycursor11213.execute("SELECT * from price_table")
        myresult11213=mycursor11213.fetchall()
        for x1213 in myresult11213:
            print(x1213)
        ffno=int(input("Enter the number of flavour you want to update prices for: "))
        ffcup=int(input("Enter new price for a cup of this flavour: "))
        ffcone=int(input("Enter new price for a cone og this flavour: "))
        
        mycursor56=mydb.cursor()
        sql56="UPDATE price_table SET cup_price=%s,cone_price=%s WHERE sr_no=%s"%(ffcup,ffcone,ffno)
        mycursor56.execute(sql56)
        mydb.commit()
        print(mycursor56.rowcount, "record(s) affected")
    
#command for action 6 i.e. show all the records 
    elif option==6:
            mycursor1124=mydb.cursor()
            mycursor1124.execute("SELECT * from records")
            myresult1124=mycursor1124.fetchall()
            print ("*"*70)
            print("Total no of orders placed : ",mycursor1124.rowcount)
    
            for x124 in myresult1124:
                print(x124)
                
        
#command for action 7 i.e. exit
    elif option==7:
        lol="no"
        print("----------THANK YOU----------")
   
        

    else:
        print("Invalid option")
        lol="yes"