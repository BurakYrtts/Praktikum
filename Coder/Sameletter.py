def has_duplicate_letter(input_string):
    letter_count = {}

    for letter in input_string:
        # Check if the letter is already in the dictionary
        if letter in letter_count:
            # If yes, it means the letter is repeated
            return True
        else:
            # If not, add the letter to the dictionary
            letter_count[letter] = 1

    # If the loop completes without returning, no duplicate letters were found
    return False

user_input = input("Enter a string: ")
if has_duplicate_letter(user_input):
    print("There is atleast 1 duplicated letter. ")
else:
    print("Nah. ")