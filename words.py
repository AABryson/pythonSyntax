words = ["hello", "hey", "goodbye", "yo", "yes"]

def print_upper_words(words):
    """For each word in list, print as uppercase."""
    for word in words:
        print(word.upper())

print_upper_words(words)


def print_words_with_e(words):
    """For each word in list, print if 'e' is in word"""
    for word in words:
        if 'e' in word:
            print(word)

print_words_with_e(words)


def print_words_first_letter(words):
    """For each word in list, print word if 'h' or 'y' is first letter"""
    # must_start_with = {'h', 'y'}
    for word in words:
        if 'h' is word[0] or 'y' is word[0]:
            print(word.upper())

print_words_first_letter(words)