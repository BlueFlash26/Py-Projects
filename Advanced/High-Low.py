from numpy.random import randint

def high_low():
    comp_points = 0
    user_points = 0

    for rounds in range(1, 6):
        #print(f"scores: computer = {comp_points} user = {user_points}")
        print(f"round {rounds}/5")

        comp_number = randint(1, 100)
        user_number = randint(1, 100)
        while user_number == comp_number:
            comp_number = randint(1, 100)
            user_number = randint(1, 100)
        
        print(f"Your number is {user_number}")
        guess = input("High or Low? ")
        while True:
            if guess.lower() == "high" or guess.lower() == "low":
                break
            else:
                print("You can only choose between low or high.")
                guess = input("High or Low? ")

        if guess.lower() == "high":
            if comp_number < user_number:
                print(f"Congrats! Your guess is right. computer number was {comp_number}")
                user_points += 1
            elif comp_number > user_number:
                print(f"Wrong! computer number was {comp_number}")
                comp_points += 1
        elif guess.lower() == "low":
            if comp_number > user_number:
                print(f"Congrats! Your guess is right. computer number was {comp_number}")
                user_points += 1
            elif comp_number < user_number:
                print(f"Wrong! computer number was {comp_number}")
                comp_points += 1

    if comp_points < user_points:
        print(f"scores: computer = {comp_points} user = {user_points}")
        print("You Won!")
    elif comp_points > user_points:
        print(f"scores: computer = {comp_points} user = {user_points}")
        print("You Lose")
    else:
        print("It's a Draw!")

high_low()