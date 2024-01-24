# proper crud project
import json
import os
def Email_data():
    while True:
        email=input("Enter Your email  :->")
        flag=0
        flag1=0
        flag2=0
        if len(email)>=6:
            if email[0].isalpha():
                if ("@" in email) and (email.count("@")==1):
                    if (email[-4]==".") ^ (email[-3]=="."):
                        for i in email:
                            if i==i.isspace():
                                flag=1
                            elif i.isalpha():
                                if i==i.upper():
                                    flag1=1
                            elif i.isdigit():
                                continue
                            elif i=="_" or i=="." or i=="@":
                                continue
                            else:
                                flag2=1
                        if flag==1:
                            print("Space is present Your Email") 
                        elif flag1==1:
                            print("Upper is present Your Email")
                        elif flag2==1:
                            print("Wrong Email")
                        else:
                            return email
                            break
                    else:
                        print("dot(.) is not present your email")
                else:
                    print("Not present @ in your email")
            else:
                print("Your first letter is not alphabet")
        else:
            print("Wrong Email lenght is less") 
            

main_dict={}
def save_data(data):
    m=json.dumps(data, indent=5)
    with open("dat.json", "w") as file:
        file.write(m)
        return m

file_name = "dat.json"
if os.path.exists(file_name):
        open_file = open("dat.json",'r')
        file_data = open_file.read()
        main_data = json.loads(file_data)
else:
        json_data = json.dumps(main_dict,indent=5)
        with open(file_name, 'w') as main_data:
            main_data.write(json_data)
        open_file = open("dat.json",'r')
        file_data = open_file.read()
        main_data = json.loads(file_data)
print("Welcome To Crud Operation  ")
while True:
    print("1 :-> Create\n2 :-> Read\n3 :-> Update\n4 :->Delete\n5 :->Break")
    choose=input("Choose Your option :->")
    if choose=="1":
        name=input("Enter Your name :->")
        Email=Email_data()
        while True:
            mobile1=input("Enter Your Phone number :->")
            if mobile1 in main_data.keys():
                print("Account With this number Already Exists")
            else:        
                if len(mobile1)==10:
                            if ("1"in mobile1 or "2"in mobile1 or "3"in mobile1 or"4"in mobile1 or 
                 "5"in mobile1 or "6" in mobile1 or "7" in mobile1 or "8" in mobile1 or 
                "9" in mobile1 or "0" in mobile1):
                                mobile=mobile1
                                break
                            else:
                                print("Phone number is not valid")
                else:
                    print("your Phone number digit is not enough")
        while True:
                password1=input("Enter Your strong password:->")
                if (
                        any(char.isupper() for char in password1)
                        and any(char.islower() for char in password1)
                        and any(char.isdigit() for char in password1)
                        and any(char in "~!@#$%^&*_" for char in password1)
                        ):
                        password = password1
                        break
                else:
                        print("Password is not valid")

        main_data.update({mobile:{"name":name,"Email":Email,"Password":password}})
        file_data = json.dumps(main_data,indent=4)
        with open("dat.json","w") as file:
              file.write(file_data)
    elif choose=="2":
        phone=input("Enter Your phone Number :->")
        if phone in main_data.keys():
            passw=input("Enter Your Password     :->")
            if passw in main_data[phone]["Password"]:
                print("what do you want ? :->\n1 :->name\n2 :->Email\n3 :->Password\n4 :-> all\n5:->break")
                choose2=int(input("Choose your option :->"))
                if choose2==1:
                        print(main_data[phone]["name"])
                elif choose2==2:
                        print(main_data[phone]["Email"])
                elif choose2==3:
                        print(main_data[phone]["Password"])
                elif choose2==4:
                        print(main_data[phone])
                elif choose2==5:
                    break
                else: 
                    print("Choose correct number")
            else:
                  print("Your Password is wrong")
        else:
            print("Your Phone Number is wrong")
    elif choose=="3":
        print("Update Your account ")
        print("1 :-> name\n2 :->Email\n3 :->password\n4 :->Mobile\n5 :->Exits")
        choose1=input("Choose Your Option :->")
        if choose1=="1":
            phone1=input("Enter Your phone Number :->")
            if phone1 in main_data.keys():
                passw=input("Enter Your Password     :->")
                if passw in main_data[phone1]["Password"]:
                    name1=input("Enter new name :->")
                    main_data[phone1]["name"]=name1
                    save_data(main_data)
                    print("Insert name successfully")
                else:
                    print("Your Password is wrong")
            else:
                 print("Phone number is wrong")
        elif choose1=="2":
            phone1=input("Enter Your Phone number :->")
            if phone1 in main_data.keys():
                passw=input("Enter Your Password       :->")
                if passw in main_data[phone1]["Password"]:
                    Email=Email_data()
                    main_data[phone1]["Email"]=Email
                    save_data(main_data)
                    print("Insert Email successfully")
                else:
                     print("Your Password is wrong")
            else:
                 print("Phone number is wrong")
        elif choose1=="3":
            phone1=input("Enter Your Phone number :->")
            if phone1 in main_data.keys():
                passw=input("Enter Your Password       :->")
                if passw in main_data[phone1]["Password"]:
                    while True:
                        name1=input("Enter new Password :->")
                        if (
                                    any(char.isupper() for char in name1)
                                    and any(char.islower() for char in name1)
                                    and any(char.isdigit() for char in name1)
                                    and any(char in "~!@#$%^&*_" for char in name1)
                                    ):
                                     
                                    main_data[phone1]["Password"]=name1
                                    save_data(main_data)
                                    print("Insert Email successfully")
                                    break
                        else:
                                    print("Password is not valid")
                else:
                     print("Your Password is wrong")
                 
            else:
                  print("Your Mobile number is wrong ")
        elif choose1=="4":
            phone1=input("Enter Your Old Phone number :->")
            if phone1 in main_data.keys():
                 Passw=input("Enter Your Password:->")
                 if Passw in main_data[phone1]["Password"]:
                    while True:
                        name1=input("Enter new mobile number :->")
                        if name1 in main_data.keys():
                             print("This number's acount is already exits")
                        else:
                            if len(name1)==10:
                                            if ("1"in name1 or "2"in name1 or "3"in name1 or"4"in name1 or 
                                "5"in name1 or "6" in name1 or "7" in name1 or "8" in name1 or 
                                "9" in name1 or "0" in name1):
                                                main_data[name1]=main_data[phone1]
                                                del main_data[phone1]
                                                save_data(main_data)
                                                print("Insert Phone Number successfully")
                                                break
                                            else:
                                                print("Phone number is not valid")
                            else:
                                print("your Phone number digit is not enough")
                 else:
                      print("Your Password is wrong")
            else:
                    print("Phone number is wrong")
        elif choose1=="5":
             pass
        else:
              print("Choose correct option")

    elif choose=="4":
            phone1=input("Enter Your Phone number :->")
            if phone1 in main_data.keys():
                passw=input("Enter your password  :->")
                if passw in main_data[phone1]["Password"]:
                    main_data.pop(phone1)
                    save_data(main_data)
                    print("Delete successfully")
                else:
                     print("Password is wrong")
            else:
                 print("Phone number is wrong")
    elif choose=="5":
          break
    else:
            print("Choose Correct Operation")



