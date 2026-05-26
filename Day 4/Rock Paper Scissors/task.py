import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")

if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
elif choice == "2":
    print(scissors)
else:
    print("Wrong Choice ")

print ("Computer Choose:")
list_of_choices = [rock, paper, scissors]
computer_choice = (random.choice(list_of_choices))
print(computer_choice)

if computer_choice == rock and choice == "0":
    print("Draw")
elif computer_choice == rock and choice == "1":
    print("You lose")
elif computer_choice == rock and choice == "2":
    print("You win")
elif computer_choice == paper and choice == "0":
    print("You lose")
elif computer_choice == paper and choice == "1":
    print("Draw")
elif computer_choice == paper and choice == "2":
    print("You win")
elif computer_choice == scissors and choice == "0":
    print("You lose")
elif computer_choice == scissors and choice == "1":
    print("You win")
elif computer_choice == scissors and choice == "2":
    print("Draw")
else:
    print("Something went wrong")

