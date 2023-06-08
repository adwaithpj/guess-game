from word_fetch import get_lower_word


def get_num_attempts():
    while True:
        num_attempts=input("How many incorrect attempts do you want [1-25]")
        
        try:
            num_attempts=int(num_attempts)

            if 1<=num_attempts<=25:
                return num_attempts
            else:
                print("{} is not between 1 and 25".format(num_attempts))

        except ValueError:
            print("{} is not an integer between 1 and 25".format(num_attempts))
_no_of_attempts_=get_num_attempts()
print("You have {} number of attempts ".format(_no_of_attempts_))

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

        
            
    


