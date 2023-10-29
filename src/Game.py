
# Task 1( ROCK,PAPER,SCISSOR )
import random as ra
def play():
    print("Welcome to the Rock Paper Scissor Game")
    user_score=0
    computer_score=0
    while True:
        user_choose=input("Enter your choice?" "(Rock,paper,scissor)")
        computer_option=("Rock", "paper","scissor")
        computer_trun= ra.choice(computer_option)
        print(f"Your turn {user_choose} \nComputer turn {computer_trun}")

        if user_choose == computer_trun:
            print("Game tie")
        elif user_choose == "scissor":
            if computer_trun == "paper":
                print("You win ,cause scissor cuts paper")
                user_score+=1
                print("Your score:",user_score) 
            else:
                print(f"Opps! You lose, cause scissor beats paper \nGood luck for the next trun")   
                computer_score +=1
                print("Computer score:",computer_score)
        elif user_choose == "paper":
            if computer_trun == "Rock":
                print("You win, cause paper covers the Rock")
                user_score+=1
                print("Your score:",user_score) 
            else:
                print(f"opps! You lose, cause paper beats Rock \nGood luck for the next trun")
                computer_score+=1
                print("Computer score:",computer_score)
        elif user_choose =="Rock":
            if computer_trun == "scissor":
                print("You win, cause Rock distroy scissor")  
                user_score+=1
                print("Your score:",user_score)
            else:
                print(f"Opps! You lose, cause Rock beats scissor \nGood luck for the next trun")
                computer_score+=1
                print("Computer score:",computer_score)

        play_again= input("Do you want to play this game again?(Yes/No)")
    
        if not play_again.lower() == "yes":
            break
        else:
            continue
    if user_score>computer_score:
        print("You are winner")  
    else:
        print("Computer are winner ,Try best for next time!")    
    print("Game over")