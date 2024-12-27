from numpy.random import randint


class Player:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__score = 0

    def update_score(self, points: int):
        self.__score += points

    def get_score(self):
        return self.__score


class Game:
    def __init__(self, rounds: int, player: Player):
        print(f"{player.name} Welcome to High or Low game!\n ----------------")
        self.rounds = rounds
        self.__attempts = 1
        self.__wins = 0
        self.__loses = 0
        self.player = player

    def play_round(self):
        comp_number = randint(1, 100)
        user_number = randint(1, 100)

        print("Your number is", user_number)
        guess = input("Do you think your number is higher or lower than my number?(higher/lower) ").strip().lower()

        while True:
            if guess == "higher":
                if comp_number < user_number:
                    print(f"You were right! computer number was {comp_number}")
                    self.__wins += 1
                elif comp_number > user_number:
                    print(f"Wrong! computer number was {comp_number}")
                    self.__loses += 1
                break
            elif guess == "lower":
                if comp_number > user_number:
                    print(f"You were right! computer number was {comp_number}")
                    self.__wins += 1
                elif comp_number < user_number:
                    print(f"Wrong! computer number was {comp_number}")
                    self.__loses += 1
                break
            else:
                guess = input("You can only choose higher or lower: ")

    def play_game(self):
        while self.__attempts <= self.rounds:
            print(f"Round: {self.__attempts} / {self.rounds}")
            self.play_round()
            self.__attempts += 1
        print(f"scores: {self.player.name} {self.__wins} computer {self.__loses}")

        if self.__wins > self.__loses:
            self.player.update_score(1)
            print("You won!")
            self.result = "won"
        elif self.__wins < self.__loses:
            print("You lose!")
            self.result = "lose"
        elif self.__wins == self.__loses:
            print("It's a draw!")
            self.result = "draw"

while True:
    play_game = input("Start game? ").lower().strip()
    if play_game == "yes" or play_game == "start":
        name = input("Your name: ")
        age = int(input("Your age: "))
        rounds = int(input("Enter number of rounds "))
        player1 = Player(name, age)
        game = Game(rounds, player1) 
        game.play_game()
    else:
        break