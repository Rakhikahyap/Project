import random
def hangman():
        print("**WELCOME! IN 'HANGMAN' GAME**")
        print("**This is word guessing game**")
        print("!You have only 10 changes for guess the correct word!")
        name=input("Enter your name: ")
        print("**WELCOME!**", name)
        list_of_word=['eduyear','hangman','india','laptop']
        word=random.choice(list_of_word)
        turns=8
        guessmade=""  
        valied_entry=set('abcdefghijklmnopqrstuvwxyz')
        while len(word)>0:
                main_word=""

                for letter in word:                          
                        if letter in guessmade:
                                main_word=main_word+letter
                        else:
                                main_word=main_word +"_"
                if main_word==word:
                        print(main_word)
                        print("You won!!!!")
                        break
                
                print("Guess the word",main_word)
                guess=input()
                
                if guess in valied_entry:
                        guessmade=guessmade+guess
                else:
                        print("Enter correct Character")
                        guess=input()
                if guess not in word:
                        turns=turns-1

                        if turns==9:
                                print("9 turns left")
                        if turns==8:
                                print("8 turns left")
                                print("     O      ")
                        if turns==7:
                                print("7 turns left")
                                print("      O      ")
                                print("      |       ")
                       
                        if turns==6:
                                print("6 turns left")
                                print("        O         ")
                                print("        |          ")
                                print("       /           ")
                        if turns==5:
                                print("5 turns left")
                                print("                   ")
                                print("          O        ")
                                print("          |         ")
                                print("         / \       ")

                        if turns==4:
                                print("4 turns left")
                                print("                 ")
                                print("         O       ")
                                print("        \|       ")
                                print("        / \      ")
                        if turns==3:
                                print("3 turns left")
                                print("                 ")
                                print("         \O/     ")
                                print("          |      ")
                                print("         / \     ")

                        if turns==2:
                                print("2 turns left")
                                print("                ")
                                print("         \O/ |  ")
                                print("          |     ")
                                print("         / \   ")

                        if turns==1:
                                print("1 turns left !!! hangman on his last breath")
                                print("                ")
                                print("         \O/_|  ")
                                print("          |     ")
                                print("         / \    ")
                        if turns==0:
                                print("You loose")
                                print("you let a good man die")
                                play_again=input("Do you want to play again 'Y' or 'N'")
                                if play_again=='Y':
                                        hangman()
                                else:
                                        print("Thanks for play this game")
                                        break
hangman()









  