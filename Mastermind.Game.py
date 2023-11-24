import random

#generating a random 4-digit number
def generate_number():
    return random.randint(10, 11)


#calculates the correct digits
def get_correct_digits(secret, guess):
    return sum(s == g for s, g in zip(str(secret), str(guess)))


#intializing the secret_p1 number
def play_game():
    print("Welcome to the Mastermind Game!")
    secret_p1 = generate_number()
    
    
    def take_turn(player):
        nonlocal secret_p1
        attempts = 0
        

        #player's turn to guess
        while True:
            guess = int(input(f"Player {player}, take a guess: "))
            attempts += 1
            
            if guess == secret_p1:
                print(f"Congratulations, Player {player}! You guessed the number in {attempts} attempts.")
                break
            
            correct_digits = get_correct_digits(secret_p1, guess)
            print(f"Correct digits: {correct_digits}. Try again.")
    
    take_turn(2)
    secret_p1 = generate_number()
    take_turn(1)

# Start the game
play_game()