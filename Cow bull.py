import random
print("::WELCOME TO COW AND BULL::")
print("::this is word guess::")
print("**you have only 7 chance**")
secret_number =list(range(5))
random.shuffle(secret_number)

# print("Guess the number. It contains 2 digits.")
print(secret_number)
# print("WELCOME TO NAME")
chance = 7
 
while chance > 0:
   player_guess = input("Enter your guess: ")
   
   if player_guess == secret_number:
       print([secret_number])
       print("Yay, you guessed it!")
       print()
       print("YOU WIN.")
       break
   else:
       bulls = 0
       l=[]
       cows = 0
      
       if player_guess[0] == secret_number[0]:
           bulls += 1
           l.append(bulls)
       if player_guess[1] == secret_number[1]:
           bulls += 1
           l.append(bulls)
       if player_guess[0] == secret_number[1]:
           cows += 1
           l.append(cows)
       if player_guess[1] == secret_number[0]:
           cows += 1
 
       print("Bulls: ",l)
       print("Cows: ",cows)
 
       chance -= 1
 
       if chance < 1:
           print("You lost the game.")
           break







# import random
# print("**:Welcome to cow and bull**")
# print("**you have only 8 chance**")
# print("**this is word guess**")
# a=[5,7,9,8,4,3,2,1]
# def game():
#     a=random.sample([0,2,1,3,5,4,8,7],4)
#     print(a)
#     cow=[]
#     bull=[]
#     for i in range(8):
#         if bull==a:
#             print("you are winner")
#             play=input("do you want play again'y'or 'n'")
#             if play=='y':
#                 game()
#             if play=='n':
#                 print("thanks for play this game")
#                 break
#         guess_a=int(input("enter your guess num"))
#         guess_positon=int(input("enter your guess position"))
#         for i in a:
#             if guess_a in a:
#                 if guess_a in a and a.index(guess_a)==guess_positon:
#                     bull.insert(guess_positon,guess_a)
         






  




