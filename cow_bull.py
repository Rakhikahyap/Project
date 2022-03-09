import random
print("WELCOME TO COW AND BULL")
print("this is guess word")
print("you have only 6 chance")
# print("Enter your Name")
def random_num():
    number=list(range(10))
    random.shuffle(number)
    return number

# print(random_num())
def secret_num():
    num=random_num()
    secret_num=[]
    for i in  range(5):
        secret_num.append(num[i])
    return secret_num

def cow_bull():
    bull=[]
    cow=[]
    num1=secret_num()
    print(num1)
    chance=6
    
    while chance>0:
        player=int(input("enter your guss number-->>"))
        possion=int(input("enter possion of guss number--->>"))
        
        if player in num1:
            index=num1.index(player)
            if index==possion:
                if  player not in bull:
                    bull.insert(index,player)
                    print("bull",bull)

                else:
                    print("already exit")
            else:
                cow.append(player)
                print("cow",cow)
        if bull==num1:
                print("do you want again 'y'or no ")
                print("wow ! congrutulation !!you are Win")
                break
        else:
            print("you loose")
            
      
        chance-=1 
        if chance==0:
            print("you have no chance")
        else:

            print(chance,"chances are left")  
        
    print("Bull",bull)
    print("Cow",cow)


cow_bull()

        