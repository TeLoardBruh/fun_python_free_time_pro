# import some lib
# best for if else practice 
from random import randint

print("This is a Rock, Paper, Scissors game of Chance ")

player = input('rock(r),paper(p),scissors(s) ?')

print(player, 'vs', end=' ')
# setting for random chocie of cpu
cpu_chocie = randint(1, 3)

# print(cpu_chocie)
# checking which are they choosing
if cpu_chocie == 1:
    computer = 'r'
elif cpu_chocie == 2:
    computer = 'p'
else:
    computer = 's'

print(computer)

if player == computer:
    print('Draw !')
elif player == 'r' and computer == 's':
    print("PLAYER WIN !")
elif player == 'r' and computer == 'p':
    print("COMPUTER WIN !")
elif player == 'p' and computer == 'r':
    print("PLAYER WIN !")
elif player == 'p' and computer == 's':
    print("COMPUTER WIN !")
elif player == 's' and computer == 'p':
    print("PLAYER WIN !")
elif player == 's' and computer == 'r':
    print("COMPUTER WIN !")
