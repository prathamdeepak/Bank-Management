
import mysql.connector
mycon = mysql.connector.connect(host = "localhost", user ="root", password="root")
cursor = mycon.cursor()

print("")
print("")

cursor.execute("create database if not exists bank")
cursor.execute("use bank")
cursor.execute("create table if not exists B_Details( name varchar(50),age int(50),phone int(50),amount int(50),govt_id int(10),account int(10),pin int(10))")

bank=("🏦 Welcome to ABC Bank 🏦")
print(bank.center(175))

import random
print("Welcome to ABC bank, start by creating your account.")
print("")
print("")
account=random.randint(10000,99999)
pin=random.randint(1000,9999)
a=(account)
b=(pin)
while True:
    name=str(input("Enter your name : " ))
    if name.isalpha():
        break
    else:
        print("Your name can only have alphabets in it!!")

    
        
print("")
while True:
    age=str(input("Enter your age : "))
    if age.isnumeric():
        break
    else:
        print("Your age can only have numbers in it.")
print("")
while True:
    phone=str(input("Enter your phone number : "))
    n=len(phone)
    if phone.isnumeric() and n==10:
        break
    else:
        print("Your phone number can only have numbers in it and should be exactly 10 digits long")
print("")
while True:
    govt_id=str(input("Enter your Government ID : "))
    if govt_id.isalpha():
        print("The Government ID cannot have alphabets in it.")
    else:
        break
print("")

while True:
    amount=str(input("Enter the amount to be deposited in your account : "))
    if amount.isnumeric():
        break
    else:
        print("The amount can only have numbers in it.")
print("")
account=random.randint(10000,99999)
print("Your account number is - ", account)
pin=random.randint(1000,9999)
print("Your PIN is - ", pin)
st="insert into B_Details values('"+name+"',"+str(age)+","+str(phone)+","+str(amount)+","+str(govt_id)+","+str(account)+","+str(pin)+");"

cursor.execute(st)


print("Your account has been successfully created!!")
print("")
print("NAME - ", name)
print("AGE - ", age)
print("PHONE NUMBER - ", phone)
print("GOVERNMENT ID - ", govt_id)
print("AMOUNT DEPOSITED - ", amount)
print("ACCOUNT NUMBER - ", account)
print("PIN - ", pin)
print("")
print("Your account details are highly confedential, please dont forget, share or loose it, Thank You!!")
print("")
print("")
print("What would you like to do")
print("1. Go to homepage")
print("2. Exit")
choice=int(input("Enter your choice : "))
amount2=int(amount)
        
while True:
    if choice==1:
        print("")
        print("")
        print("---------------------------------------------------------------------------🏦 Welcome to ABC Bank 🏦  ------------------------------------------------------------------                                                                                    ")

        print("1.Create a new account.")
        print("2.Existing account.")
        print("3.Exit")
        ch=int(input("Enter Your choice : "))
        print("")
        if ch==3:
            print("Thank You For Banking with us !!")
            break

        while True:
            if ch==1:
                print("")
                print("")
                print("")
                print("Start by creating your account.")
                while True:
                        name=str(input("Enter your name : " ))
                        if name.isalpha():
                            break
                        else:
                            print("Your name can only have alphabets in it!!")
                print("")
                while True:
                    age=str(input("Enter your age : "))
                    if age.isnumeric():
                        break
                    else:
                        print("Your age can only have numbers in it.")
                print("")
                while True:
                    phone=str(input("Enter your phone number : "))
                    if phone.isnumeric():
                        break
                    else:
                        print("Your phone number can only have numbers in it!!")
                print("")
                while True:
                    govt_id=str(input("Enter your Government ID : "))
                    if govt_id.isalpha():
                        print("The Government ID cannot have alphabets in it.")
                    else:
                        break
                print("")

                while True:
                    amount=str(input("Enter the amount to be deposited in your account : "))
                    if amount.isnumeric():
                        break
                    else:
                        print("The amount can only have numbers in it.")
                    
                print("")
                print("Your account details are highly confedential, please dont forget, share or loose it, Thank You!!")
                a=random.randint(10000,99999)
                print("Your account number is - ", account)
                b=random.randint(1000,9999)
                print("Your PIN is - ", pin)
                print("Your account has been successfully created!!")
                print("NAME - ", name)
                print("AGE - ", age)
                print("PHONE NUMBER - ", phone)
                print("GOVERNMENT ID - ", govt_id)
                print("AMOUNT DEPOSITED - ", amount)
                print("ACCOUNT NUMBER - ", a)
                print("PIN - ", b)
                print("Your account details are highly confedential, please dont forget, share or loose it, Thank You!!")
                amount2=int(amount)
                


    
            if ch==2:
                print("Welcome back!!!")
                print("Please Log-in to continue")
                print("")
                print("")
            
                while True:
                    A=int(input("Enter your account number : "))
                    if A!=account:
                        print("Account number not found, please try again.")
                    else:
                        break
                while True:
                    B=int(input("Enter your PIN : "))
                    print("")
                    print("")
                    if B!=pin:
                        print("Incorrect pin, try again:")
                    else:
                        break

            break
        print("Welcome", name,"!!!")
        while True: 
            print("")
            print("What would you like to do")
            print("1. Check Balance.")
            print("2. Withdraw Money.")
            print("3. Deposit Money..")
            print("4. Homepage.")
            choice2=int(input("Enter your choice : "))
            if choice2==1:
                print("Current Balance - ", amount2)
                    
                
            if choice2==2:                     
                    while True:
                        wid=int(input("Enter The Amount to be Withdraw : "))
                        if wid>amount2:
                            print("Insufficient Balance !!!")
                            print("Current Balance - ", amount2)
                        else:
                            print("Successfully withdrawn", wid)
                            amount2=amount2-wid
                            print("Current Balance - ", amount2)
                            break

            if choice2==3:
                dep=int(input("Enter The Amount to be Deposited : "))
                amount2=amount2+dep
                print("Successfully deposited : ", dep)
                print("Current Balance - ", amount2)
            if choice2==4:
                break


    if choice==2:
        print("Thank You For Banking With Us !!!")
        breakpoint
    
            



 


    
   
                
