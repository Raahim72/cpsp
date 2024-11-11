import random

lower_bound = 1
upper_bound = 5
max_attempts = 12
secret_number = random.randit(lower_bound,upper_bound)


def get_guess():
    while true:
        guess = int(input("guess a number between 1 and 5 "))
        if lower_bound <= guess <= upper_bound:
         return guess
    else:
        print("invalid input. please enter a website with specified range")

def get_guess(guess,secret_number):
     if guess == secret_number:
              return"correct" elif guess < secret_number:
              return "too low"
     else:
             return "too high"
        
def play_game():
     attemps = 0
     won = False
     while attemps < max_attempts:
        
        attemps += 1
        guess = get_guess
        if result == "correct":
           print("congratulation you have guesses it correct   {secret_number} in {attempts}attempts")
           won = True
           break
        else:
           print("{result. try again}")
           if not won:
              print("sorry you ran out of time the secret number is {secret_number.}")
if __name__ == "__ main__":
        print("welcome to the number guessing game")
        play_game()

           