# import sys
# script, user_sentence = sys.argv

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# Called by print_first_and_last_sorted
# Called by print_first_and_last
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# def print_original_sentence(sentence):
#     print(f"\nYour original sentence: {sentence}")

# def enter_key_to_close():
#     print("\nCompleted - press any key to continue ...")
#     input()

# def main(sentence):
#     print_original_sentence(sentence)

#     print(f"\nThese are the sorted words: {sort_words(sentence)}")

#     print("\nPrinting the first and last words:")
#     print_first_and_last(sentence)
    
#     print("\nPrinting sorted first and last words:")
#     print_first_and_last_sorted(sentence)

#     enter_key_to_close()

# main(user_sentence)