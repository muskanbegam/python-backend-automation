import random

def guess_number(guess,num):
        if guess == num:
                print("You guessed it Right!!")
                return False
        else:
                print("oh no its a wrong guess")
                return True


print("Let's play the Guessing Game")
print("****************************")
num = random.randint(1,10)
is_play=True
trials=0

while is_play==True:
    trials += 1
    guess = int(input("Enter your guess from 1 to 10: "))
    is_play= guess_number(guess,num)

print(f"Guessed in {trials} times.")



