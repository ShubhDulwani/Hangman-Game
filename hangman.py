import random
import os

# Word categories with hints
WORD_CATEGORIES = {
    "Animals": {
        "elephant": "A large mammal with a trunk",
        "penguin": "A flightless bird that lives in cold regions",
        "dolphin": "An intelligent marine mammal",
        "kangaroo": "An Australian animal that hops",
        "butterfly": "A colorful insect with wings",
        "giraffe": "The tallest land animal",
        "octopus": "A sea creature with eight arms",
        "cheetah": "The fastest land animal"
    },
    "Countries": {
        "australia": "Home to kangaroos and koalas",
        "brazil": "Famous for carnival and Amazon rainforest",
        "japan": "Land of the rising sun",
        "egypt": "Home to pyramids and pharaohs",
        "canada": "Known for maple syrup",
        "india": "Country with the Taj Mahal",
        "france": "Famous for the Eiffel Tower",
        "mexico": "Known for tacos and ancient Mayan ruins"
    },
    "Technology": {
        "computer": "Electronic device for processing data",
        "internet": "Global network connecting millions of devices",
        "software": "Programs and applications that run on devices",
        "keyboard": "Input device with letters and numbers",
        "algorithm": "Step-by-step problem-solving procedure",
        "database": "Organized collection of data",
        "python": "Popular programming language",
        "artificial": "Type of intelligence created by humans"
    },
    "Sports": {
        "football": "Popular sport played with a round ball",
        "cricket": "Bat and ball game popular in India",
        "basketball": "Game with a hoop and orange ball",
        "swimming": "Water sport and exercise",
        "tennis": "Racket sport played on a court",
        "volleyball": "Team sport with a net",
        "badminton": "Racket sport with a shuttlecock",
        "hockey": "Game played with a stick and puck or ball"
    }
}

# Difficulty levels
DIFFICULTY_LEVELS = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}

# Hangman stages
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Display game banner"""
    print("=" * 50)
    print("       WELCOME TO HANGMAN GAME!       ")
    print("=" * 50)
    print()

def select_category():
    """Let user select a category"""
    print("Available Categories:")
    categories = list(WORD_CATEGORIES.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("\nSelect category (enter number): "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(categories)}")
        except ValueError:
            print("Invalid input! Please enter a number.")

def select_difficulty():
    """Let user select difficulty level"""
    print("\nDifficulty Levels:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    
    while True:
        try:
            choice = int(input("\nSelect difficulty (enter number): "))
            if choice == 1:
                return "easy"
            elif choice == 2:
                return "medium"
            elif choice == 3:
                return "hard"
            else:
                print("Please enter 1, 2, or 3")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_word_and_hint(category):
    """Get random word and hint from selected category"""
    word_dict = WORD_CATEGORIES[category]
    word = random.choice(list(word_dict.keys()))
    hint = word_dict[word]
    return word, hint

def display_game_state(word, guessed_letters, attempts_left, wrong_guesses):
    """Display current game state"""
    clear_screen()
    display_banner()
    
    # Display hangman
    wrong_count = len(wrong_guesses)
    if wrong_count < len(HANGMAN_STAGES):
        print(HANGMAN_STAGES[wrong_count])
    
    # Display word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"\nWord: {display_word}")
    print(f"\nAttempts Remaining: {attempts_left}")
    print(f"Wrong Guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
    print(f"Correct Guesses: {', '.join(sorted(set(word) & guessed_letters)) if guessed_letters else 'None'}")

def get_user_guess(guessed_letters):
    """Get and validate user input"""
    while True:
        guess = input("\nEnter a letter (or 'hint' for a hint, 'quit' to exit): ").lower()
        
        if guess == 'quit':
            return 'quit'
        
        if guess == 'hint':
            return 'hint'
        
        if len(guess) != 1:
            print("Please enter only one letter!")
            continue
        
        if not guess.isalpha():
            print("Please enter a valid letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        return guess

def play_game():
    """Main game loop"""
    clear_screen()
    display_banner()
    
    # Game setup
    category = select_category()
    difficulty = select_difficulty()
    word, hint = get_word_and_hint(category)
    
    max_attempts = DIFFICULTY_LEVELS[difficulty]
    attempts_left = max_attempts
    guessed_letters = set()
    wrong_guesses = set()
    hint_used = False
    
    print(f"\nCategory: {category}")
    print(f"Difficulty: {difficulty.capitalize()}")
    print(f"Word length: {len(word)} letters")
    input("\nPress Enter to start...")
    
    # Game loop
    while attempts_left > 0:
        display_game_state(word, guessed_letters, attempts_left, wrong_guesses)
        
        # Check if word is complete
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"The word was: {word.upper()}")
            print("=" * 50)
            return True
        
        # Get user guess
        guess = get_user_guess(guessed_letters)
        
        if guess == 'quit':
            print(f"\nGame ended. The word was: {word.upper()}")
            return False
        
        if guess == 'hint':
            if not hint_used:
                print(f"\nHint: {hint}")
                hint_used = True
                input("Press Enter to continue...")
            else:
                print("\nYou already used your hint!")
                input("Press Enter to continue...")
            continue
        
        # Process guess
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"\n✓ Correct! '{guess}' is in the word!")
        else:
            print(f"\n✗ Wrong! '{guess}' is not in the word!")
            wrong_guesses.add(guess)
            attempts_left -= 1
        
        input("Press Enter to continue...")
    
    # Game over
    display_game_state(word, guessed_letters, attempts_left, wrong_guesses)
    print("\n" + "=" * 50)
    print("💀 GAME OVER! YOU LOST! 💀")
    print(f"The word was: {word.upper()}")
    print("=" * 50)
    return False

def main():
    """Main function"""
    while True:
        play_game()
        
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'y']:
                break
            elif play_again in ['no', 'n']:
                print("\nThanks for playing! Goodbye! 👋")
                return
            else:
                print("Please enter 'yes' or 'no'")

if __name__ == "__main__":
    main()