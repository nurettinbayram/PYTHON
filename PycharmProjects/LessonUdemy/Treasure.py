from LessonUdemy.Shapes import treasure

print(treasure)
print('Welcome to Treasure Island. \nYour mission is to find the treasure.')
firstStep = input("You're at a cross road. Where do you want to go?\n       Type 'left' or 'right' \n").lower()
if firstStep=="left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    secondStep = input('Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if secondStep == "wait":
        print('You arrive at the island unharmed. There is a house with 3 doors.')
        thirdStep = input('One red, one yellow and one blue. Which colour do you choose?').lower()
        if thirdStep == 'yellow':
            print('you win!')
        elif thirdStep=='red':
            print('Burned by fire. Game Over.')
            #break
        elif thirdStep =='blue':
            print('Eaten by beasts. Game Over.')
        else:
            print('Game Over')


    else:
        print('Attacked by trout. Game Over.')

else:
    print("Fall into a hole. Game Over.")
    # break