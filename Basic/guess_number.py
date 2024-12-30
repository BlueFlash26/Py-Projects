from random import randint

def guess_number():
    number = randint(0, 99)

    print("I'm thinking of a number between 0-99.", end=" ")

    for attempts in range(5, 0, -1):
        user_guess = int(input("Guess the number: "))
        if user_guess == number:
            print("Congrats! the number was " + str(number))
            break  
        elif user_guess < number:
            if attempts - 1==0:
                print("Attempts finished You lost! the number was " + str(number)) 
            else:
                print(f"Wrong! {attempts -1} Tries left, " + "Your guess was too low.")
        elif user_guess > number:
            if attempts - 1==0:
                print("Attempts finished You lost! the number was " + str(number)) 
            else:
                print(f"Wrong! {attempts -1} Tries left, " + "Your guess was too high.") 
        
            
    return retry()

def retry():
    retry = input("Play again? ")
    if retry.lower() == "yes":
        guess_number()
    else:
        print("Come again!")

guess_number()

