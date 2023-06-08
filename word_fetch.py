# Function to fetch words from the text file"

import random

word_list = "wordlist.txt"

def get_lower_word(min_word_length):
    num_word_processed = 0
    curr_word=None
    with open(word_list, "r") as f: 
        # random.seed(4)        
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()

            if len(word) < min_word_length:
                continue

            num_alpha = sum(1 for c in word if c.isalpha())
            if num_alpha == min_word_length:
                num_word_processed += 1
                if random.randint(1, num_word_processed) == 1:
                    curr_word = word
        return curr_word




