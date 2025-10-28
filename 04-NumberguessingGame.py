import random
def get_user_input():
    while True: 
        try :
            user_input= int (input(" Please choose number form 1 to 10 : \n" ))
            if 1<= user_input<=10 : 
                return user_input
            else : 
                print("The number is out of range , please try again ! ")
        
        except ValueError:
            print("The number is not an integer number ❌ , please try again")
        
def play_game():
    attempts = 0 
    print("the game starts, good luck !\n")
    computer = random.randint(1,10)
    while True : 
        user = get_user_input()
        attempts +=1
        print(f"  🙎 Your number is {user}\n")

        if user == computer : 
            print( f" 🎉 Congratulations you won form attempt number {attempts} \n")
            break
        elif user <= computer : 
            print ( " Your guess is lower \n")
        elif user >= computer : 
            print ( " Your guess is higher \n")

play_game()



