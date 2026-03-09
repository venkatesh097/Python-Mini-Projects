import random as r

print("-"*20,end = "WELCOME")
print("-"*20)

a = ["Rock","Paper","Scissor"]
computer = r.choice(a)

played = 0
player_points = 0
computer_points = 0
player = input("Enter your choice('r'/'p'/'s')('q' to Quit): ")

while True:
    if player.lower() == 'q':
        break
    if player == "r":
        if computer == "Rock":
            print("Tie")
            played+=1
        elif computer == "Paper":
            print("You Win")
            player_points+=1
            played+=1
        elif computer == "Scissor":
            print("Yout lose")
            computer_points+=1
            played+=1
        else:
            print("Invalid Choice")
    elif player == "p":
        if computer == "Rock":
            print("You Lose")
            computer_points+=1
            played+=1
        elif computer == "Scissor":
            print("You win")
            player_points+=1
            played+=1
        elif computer == "Paper":
            print("Tie")
            played+=1
        else:
            print("Invalid Choice")
    elif player == "s":
        if computer == "Rock":
            print("You win")
            player_points+=1
            played+=1
        elif computer == "Scissor":
            print("Tie")
            played+=1
        elif computer == "Paper":
            print("You lose")
            computer_points+=1
            played+=1
        else:
            print("Invalid choice")
    else:
        print("Invalid Choice1")

    player = input("Enter your choice('r'/'p'/'s')('q' to Quit): ")
    computer = r.choice(a)
print("-"*20,end = "Results")
print("-"*20)

print("Player Points: ", player_points)
print("Computer Points: ", computer_points)

if player_points > computer_points:
    print("You won the round")
elif player_points < computer_points:
    print("Computer won the round")
else:
    print("Tie")

print("Number of times played: ",played)
