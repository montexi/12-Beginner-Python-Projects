import random
# The computer generates a random number between 1 and 10
# If the user's guess it too low, it returns "Too low"
# If the user's guess it too high, it returns "Too high"
def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while  guess != random_number:
        guess = int(input(f'Guess A Number Between 1 & {x}: '))
        if guess < random_number:
           print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        
    print(f'Correct! Great guess! The number was {random_number}!')


       
       

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:   
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1


    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(400) #RANGE
