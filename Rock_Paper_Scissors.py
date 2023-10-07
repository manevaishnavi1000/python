#Rock paper scissors game
import random
def rps():
    print("")
    print("************* Welcome to rock paper scissors game *************")
    print("")
    user= str(input("Enter your name : "))
    list=["rock", "paper", "scissors"]
    player_points= 0
    comp_points=0
    print("")
    print("three points to win the game")
    print("")
    while player_points<3 and comp_points<3:
        comp_choice=random.choice(list)
        player_choice=input("Rock, Paper or scissors?")
        player_choice=player_choice.lower() #convert into smaller letter
        print(f"Computer: {comp_choice} vs {user}: {player_choice}")
        print("")
        if player_choice==comp_choice:
            print("Its a tie. No points!")
            print("")
        elif player_choice=="rock":
            if comp_choice=="scissors":
                print(f"{user} wins! 1 point.")
                print("")
                player_points+=1
            elif comp_choice=="paper":
                print(f"Computer wins! 1 point.")
                print("")
                comp_points+=1
        elif player_choice=="paper":
            if comp_choice=="rock":
                print(f"{user} wins! 1 point.")
                print("")
                player_points+=1
            elif comp_choice=="scissors":
                print(f"Computer wins! 1 point.")
                print("")
                comp_points+=1
        elif player_choice=="scissors":
            if comp_choice=="paper":
                print(f"{user} wins! 1 point.")
                print("")
                player_points+=1
            elif comp_choice=="rock":
                print(f"Computer wins! 1 point.")
                print("")
                comp_points+=1
        else:
            print("Invalid statement. Try again")
            print("")
    if player_points==3:
        print(f"Final Result------>{user} wins the game!")
    else:
        print("Game over!! Final Result------> Computer Wins!")
    print("Exited rock paper scissors game")
if __name__=="__main__":
    rps()