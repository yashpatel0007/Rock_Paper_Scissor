# Rock Paper or scissor
import random
def game(comp, you):
    # if two value are equal, declare as tie
    if comp == you:
        return None

    #Check for all possibilities when computer choose 
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Comp Turn: Rock(r) Paper(p) or scissor(s)")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Rock(r) Paper(p) or scissor(s)?\n")
a = game(comp, you)

print(f"Computer choose {comp}")
print(f"You Choose {you}")
if a == None:
    print("The Game Is Tie!!!")
elif a:
    print("Great You Win")
else:
    print("You Lose!!!!")

print("Keep Playing Thanks You!")