word_bank = []  # create an empty list to store the words

while True:
    word = input("Enter a word: ")
    while not word:
        print("You have not entered a text")
        word = input("Enter a word: ")
    word_bank.append(word)

    print("You entered a word:", word)
    choice = input("Do you want to enter another word? (Y/N): ")  # asks the user if they want to put another word/s
    while choice.upper() not in ['Y', 'N']:  # if the user miss-inputs a word
        choice = input("Invalid input. Do you want to enter another word? (Y/N): ")
    if choice.upper() == 'N' and "n":
        break

print("\nYou Entered ", len(word_bank), "words")  # displays the total amount of string
for word in word_bank:
    print(word)  # displays all the stings

# https://github.com/SenpaiLuwi
