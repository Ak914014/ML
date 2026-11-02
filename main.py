import json
import random
import string
from pathlib import Path

class Bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists():

            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such files exist")
    except Exception as err:
        print(f"an error occured as {err} ")
    
    @classmethod
    def __update(cls):
        with open (cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k =3)
        num = random.choices(string.digits, k =3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)   


    def Createaccount(self):
        info = {
            "name":input("Tell your name :- "),
            "age": int(input("Tell your age :-")),
            "email": input("Tell me your email :-"),
            "pin": int(input("tell me your 4 number pin :-")),
            "accountNo.": Bank.__accountgenerate( ),
            "balance":0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4 :
            print("sorry you can not create your account")

        else:
            print("account is created !!")

            for i in info:
                print(f"{i}: {info}")
            
            print("Please not down your account number")
            Bank.data.append(info)
            Bank.__update()

    
    def Deposite(self):

        accNumber = input("Please give me your accont number :- ")
        pin = int(input("please give me your pin :-"))
      
        userdata = [i for i in Bank.data if i['accountNo.'] == accNumber and i['pin'] == pin]
        if userdata == False:
            print("sorry no data found")
        else:
            amount = int(input("how much you want to deposite :-"))

            if amount > 10000 or amount < 0:
                print("sorry you can't give this amount")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Deposite successfully !! ")
        
    
    def Withdraw(self):
        
         accNumber = input("Please give me your accont number :- ")
         pin = int(input("please give me your pin :-"))
      
         userdata = [i for i in Bank.data if i['accountNo.'] == accNumber and i['pin'] == pin]
         if userdata == False:
            print("sorry no data found")
         else:
            amount = int(input("how much you want to withdraw :-"))

            if  userdata[0]['balance']< amount  and amount< 0:
                print("sorry you can't withdraw this amount")

            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("withdrew successfully !! ")



    def Details(self):

         accNumber = input("Please give me your accont number :- ")
         pin = int(input("please give me your pin :-"))
      
         userdata = [i for i in Bank.data if i['accountNo.'] == accNumber and i['pin'] == pin]
         if userdata == False:
            print("sorry no data found")
         else:
            # print(userdata)
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]} ")


    def updateDetails(self):
        accNumber = input("Please give me your account number :- ")
        pin = int(input("Please give me your pin :- "))

        userdata = [
            i for i in Bank.data
            if i['accountNo.'] == accNumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")
            return

        print("You can't change the age, account number, and balance")
        print("Press 1 for Name")
        print("Press 2 for Email")
        print("Press 3 for Pin")

        num = int(input("Give the number :- "))

        if num == 1:
            name = input("Give the new name :- ")
            userdata[0]['name'] = name

        elif num == 2:
            email = input("Give the new email :- ")
            userdata[0]['email'] = email

        elif num == 3:
            new_pin = int(input("Give the new 4 digit pin :- "))

            if len(str(new_pin)) != 4:
                print("Pin must be exactly 4 digits")
                return

            userdata[0]['pin'] = new_pin

        else:
            print("Your input is wrong")
            return

        Bank.__update()
        print("Update successfully !!")

    def DeleteAccount(self):
        accNumber = input("Please give me your account number :- ")
        pin = int(input("Please give me your pin :- "))

        userdata = [
            i for i in Bank.data
            if i['accountNo.'] == accNumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")
            return

        else:
            Bank.data.remove(userdata[0])
            Bank.__update()

            print("Account deleted")

 

print("press 1 for creating an account")
print("press 2 for Depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting an account")


check  = int(input("tell your response :-"))

user = Bank()
if check == 1:
    user.Createaccount()

if check == 2:
    user.Deposite()

if check == 3:
    user.Withdraw()

if check == 4:
    user.Details()

if check == 5:
    user.updateDetails()

if check == 6:
    user.DeleteAccount()    