import random

while True:
  print("Make your choice: 'R' for rock, 'P' for paper, 'S' for scissors")
  
  user_choice = input("Enter R, P or S:" )
  CHOICES = ["R", "P", "S"]
  computer_choice = random.choice(CHOICES)
  print(f"\nYou Chose '{user_choice}', and the computer chose '{computer_choice}'.\n")

   
  if user_choice == computer_choice:
    print(f"You and the computer selected '{user_choice}'. It's a tie!")
        
  elif user_choice == "R":
        if computer_choice == "S":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
  elif user_choice == "P":
        if computer_choice == "R":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
  elif user_choice == "S":
        if computer_choice == "P":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")
  else:
    print(f"\n'{user_choice}'isn't a valid input")  
    again = input("\nPlay again? (yes/no): ")
    if again.lower() == "no":
         break
    print() 
    
print("\n Goodbye")