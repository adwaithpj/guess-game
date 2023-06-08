from word_fetch import get_lower_word


def get_num_attempts():
    while True:
        num_attempts=input("How many incorrect attempts do you want [1-25]\n")
        
        try:
            num_attempts=int(num_attempts)

            if 1<=num_attempts<=25:
                return num_attempts
            else:
                print("{} is not between 1 and 25".format(num_attempts))

        except ValueError:
            print("{} is not an integer between 1 and 25".format(num_attempts))


def get_min_word_length():
    # This function is to get a word of desired length


    while True:
        min_word_length=input("What is the minimum length of the word you want [4-16] ?")

        try:
            min_word_length=int(min_word_length)
            if 4<=min_word_length<=16:
                return min_word_length
        except ValueError:
            print("Entered value {} is not the form of a integer!!")    

        
def play_guessggame():
    print("Welcome to Guess game")
    min_word_len= get_min_word_length()
    print("Minimum no of words = {}".format(min_word_len))            
    no_of_attempts_= get_num_attempts()
    print("You have {} number of attempts ".format(no_of_attempts_))
    
    # Fetching a word of minimum length from text file
    word = get_lower_word(min_word_len).rstrip()
    guessed_letters = []
    correct_letters =[]
    game_over = False

    while not game_over:
        print("\nWord "," ".join([letter if letter in guessed_letters else "_" for letter in word]))

        if len(correct_letters) ==  len((word)):
            print("\nCongratulations! You gussed the word correctly!")
            break

        #
        print("\nAttempts remaining : ",no_of_attempts_)
        guess = input("Enter a letter : ").lower()

        if guess in guessed_letters:
            print("\nYou have already guessed that letter!!")

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            correct_letters.append(guess)
        else:
            print("Wrong guess!")
            no_of_attempts_ -= 1
            if no_of_attempts_ == 0:
                print("\nGame over! You ran out of attempts.")
                print("The word was:", word)
                break




play_guessggame()
    


