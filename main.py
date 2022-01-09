import functions, sys
while True: # main program loop
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = input("Enter a string to get some information about it, \"exit\" to exit program:  ")
    if message != "exit":
        count = functions.get_chars(message) # return a dictionary of the count of each different character in message
        sortedkeys = sorted(count, key=lambda x:x.lower()) #creates a sorted list of the keys from the count dictionary
        sorteddict = functions.create_sorted_dict(sortedkeys, count) # takes the sorted_keys and grabs the matching values from the original count dictionary
        numofchars = functions.char_count(message) # get number of unique non-punctuation characters in message
        print(sorteddict)
        print("The string \"{string}\" is {length} characters long and has {numchars} different characters.".format(string=message, numchars=numofchars, length=str(len(message))))
    else:
        sys.exit("byebye")
    while True: # loop for secondary functions on original user input
        user_question = input("Press \"1\" to jump to character queries, \"0\" to go back to main, \"exit\" to exit program")
        if user_question == "1":
            while True: # loop for character queries on original user input
                lower_message = message.lower()
                char_query = input("Enter a character to query, \"0\" to go back, \"exit\" to exit program")
                if char_query != "0" and char_query != "exit":
                    print("There are {occurences} occurences of {char} in \"{message}\"".format(occurences=functions.char_occurences(lower_message, char_query), char=char_query, message=message))
                    if char_query.lower() in alphabet:
                        lower_char = char_query.lower()
                        print("The letter {lower_char} is the {index} letter in the alphabet.".format(lower_char=lower_char, index=functions.index_in_alphabet(lower_char, alphabet)))
                elif char_query == "0":
                    break
                elif char_query == "exit":
                    sys.exit("byebye")
        elif user_question == "0":
            break
        elif user_question == "exit":
            sys.exit("byebye")