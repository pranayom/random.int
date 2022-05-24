#Creating a rock papers scissors project
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

#Write your code below this line 👇
import random
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
comp_choice  = random.randint(0,2)
display = [rock, paper, scissors]
decision_pair = (int(player_choice), comp_choice)
print("Player chooses", display[int(player_choice)])
print("Computer chooses", display[int(comp_choice)])
      
player_win = [(0,2),(1,0),(2,1)]
comp_win = [(2,0),(0,1),(1,2)]
if decision_pair in player_win:
  print("Player wins")
elif decision_pair in comp_win:
  print("Computer wins")
else: print("Its a draw")
