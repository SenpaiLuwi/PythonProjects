def palindrome(input_string):
    reversed_string = input_string[::-1]  # reverse the string
    capitalized_string = reversed_string.upper()  # capitalize each letter
    return capitalized_string


def display_reversed_words(words):
    print("Word   Revered")
    print("----------------")
    for i, word in enumerate(words, start=1):
        print(f"{i}. {word}   {palindrome(word).strip()}")


# main program
words = []
while True:
    input_word = input("Enter a word (or 'q' to quit and show the Word and Reversed Word): ")
    if input_word.lower() == 'q':
        break
    words.append(input_word)

print()
display_reversed_words(words)
