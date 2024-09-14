import random  # Import the random module

n = random.randint(1, 100)  # Randomly generate a number between 1 and 100 and assign it to 'n'
a = -1  # Initialize variable 'a' to -1, this will store the user's guess
guesses = 1  # Initialize the guess count to 1

# Start a loop that continues until the user guesses the correct number
while a != n:
    a = int(input("Guess the number: "))  # Take input from the user and convert it to an integer
    
    # If the user's guess is greater than the randomly chosen number
    if a > n:
        print("Lower number please")  # Hint that the number is lower
        guesses += 1  # Increment the guess counter
    
    # If the user's guess is smaller than the randomly chosen number
    elif a < n:
        print("Higher number please")  # Hint that the number is higher
        guesses += 1  # Increment the guess counter

# When the loop breaks (i.e., the guess is correct), print a success message with the number of attempts
print(f"You have guessed the number {n} correctly in {guesses} attempts")