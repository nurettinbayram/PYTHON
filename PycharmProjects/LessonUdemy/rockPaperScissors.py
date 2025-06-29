from LessonUdemy.Shapes import rockPaperScissors
import random

chooses =int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

print(rockPaperScissors[chooses])
print('computer choose:')
computer_Choose = int(random.randint(0,2))
print(rockPaperScissors[computer_Choose])

if (computer_Choose==0 and chooses==1) or (computer_Choose==1 and chooses==2) or (computer_Choose==2 and chooses==0):
    print("you win!")
elif (computer_Choose == 1 and chooses == 0) or (computer_Choose == 2 and chooses == 1) or (
        computer_Choose == 0 and chooses == 2):
    print("computer win!")
else:
    print("draw")
