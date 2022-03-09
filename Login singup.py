import json
start=input("enter a 1 login|2 signup!!")
if start=='1':
    a={}
    username=input("Enter a Username: ")
    password=input("Enter Your Password: ")
    digit,special,upper,lower=0,0,0,0
    if len(password)>=6:
        for i in password:
            if (i.isupper()):
                upper=1
            if (i.islower()):
                lower=1
            if (i.isdigit()):
                digit=1
            if(i=='@'or i=='$' or i=='_' or i=='#' or i=="!" or i=="%" or i=="&" or i=="*"):
                special=1
            total=upper+digit+lower+special
        if total!=4:
            print("Password Contains One Special Character, One Capital Letter, One Small Letter and One Digit! ")
        else:
            password1=input("confirm password")
            if password==password1: 
                gender=input("Enter Your Gender 'Male' and 'Female': ")
                dob=input("Enter Your DOB: ")
                a['name']=username
                a['password']=password
                a['gender']=gender
                a['DOB']=dob
                with open("UserDetails.json","w") as f:
                    json.dump(a,f,indent=4)
                    print("You are Logged in Successfully!")
            elif password!=password1:
                print("password dosn't match,restart!!")
    else:
        print("the password should be contain 6 character")             
elif start=='2':
    a={}
    username=input("Enter a Username: ")
    password=input("Enter Your Password: ")
    upper,lower,digit,special=0,0,0,0
    if len(password)>=6:
        for i in password:
            if (i.isupper()):
                upper=1
            if (i.isdigit()):
                digit=1
            if (i.islower()):
                lower=1
            if(i=='@'or i=='$' or i=='#' or i=="!" or i=="%" or i=="&" or i=="*" ):
                special=1
            total=upper+digit+lower+special 
        if total!=4:
            print("password should contain atlest one upper, lower,digit,special caracter")
        else:
            with open("UserDetails.json","r") as f:
                file=f.read()
                if username in file:
                    print("you are already login here")
                else:
                    password1=input("confirm password")
                    if password==password1: 
                        gender=input("Enter Your Gender 'Male' and 'Female': ")
                        dob=input("Enter Your DOB: ")
                        a['name']=username
                        a['password']=password
                        a['gender']=gender
                        a['DOB']=dob
                        with open("UserDetails.json","w+") as f:
                            json.dump(a,f,indent=4)
                            print("You are Logged in Successfully!")
                    elif password!=password1:
                        print("password dosn't match,restart!!")
    else:
        
        print("the password should be contin 6 character!!")

