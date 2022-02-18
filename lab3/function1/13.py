import random


name=input('Hello! What is your name?\n')
number=random.randint(1,20)
#print(number)
guess=int(input(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n'))
cnt=1
if guess!=number:
    while(guess!=number):
        guess=int(input("Your guess is too low.\nTake a guess.\n"))
        cnt+=1
    else:
      print(f"Good job, {name}! You guessed my number in {cnt} guesses!")    
      

else: print(f"Good job, {name}! You guessed my number in 1 guesses!")    
'''
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
'''
