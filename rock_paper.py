import random

user_score = 0
computer_score = 0

while True:
    print("\nRock Paper Scissors Game 🪨 📃 ✂️\n")
    print("Choose:")
    print("rock | paper | scissors")
    user = input("Your choice: ").lower()
    
    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])
    emoji = {"rock":"🪨", "paper":"📃", "scissors":"✂️"}

    print("Computer choice💻:", computer, emoji[computer])

    if user == computer:
        print("It's a tie! 🫱🏼‍🫲🏻")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round! 💃🏻")
        user_score += 1
    else:
        print("Computer wins this round! 🤖")
        computer_score += 1

    print("Your score:", user_score, "| Computer score:", computer_score)

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing🎮!!")
        break
