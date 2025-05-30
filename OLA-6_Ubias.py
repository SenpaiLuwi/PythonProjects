def palindrome(input_string):
    reversed_string = input_string[::-1]  # reverse the string
    capitalized_string = reversed_string.upper()  # capitalize each letter
    return capitalized_string


# get input from user
input_word = input("Enter a word:")

# call the reverse_and_capitalize function
reversed_word = palindrome(input_word).strip()

# display results
print(f"INPUT: {input_word}")
print(f"REVERSED:{reversed_word} ({len(reversed_word)} characters)")
