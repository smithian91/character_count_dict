def get_chars(message):  # creates a dictionary of the count of each unique non-punctuation character in message
    count = {}
    punctuation = "!?., \'\""
    for character in message:
        if character not in punctuation:
            count.setdefault(character, 0)
            count[character] += 1

    return count


def create_sorted_dict(keys, count):  # takes a list of keys and a dictionary with count, returns a sorted dictionary
    output_dict = {}
    for i in keys:
        output_dict[i] = count[i]
    return output_dict


def char_count(message):  # returns the number of unique non-punctuation characters in message
    punctuation = "!?., \'\""
    numofchars = 0
    already_counted = ""
    for char in message:
        if char not in punctuation and char not in already_counted:
            numofchars += 1
            already_counted = already_counted + char
    return numofchars


def char_occurences(message, char):  # returns the count of a particular character in message
    count = 0
    for i in message:
        if i == char:
            count += 1
    return count


def index_in_alphabet(char, alphabet):  # returns the index of the 1st character in the char string relative to the alphabet
    char_lower = char[0].lower()
    char_index = alphabet.index(char_lower)
    return (char_index + 1)


