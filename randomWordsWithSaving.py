###IMPORTS###

import random

###VARIABLES###

words = [] # List of generated "words"
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split() # A list of letters to use
wordLength = int(input("What will be the length of one word: ")) # Get the length of a word
wordCount = int(input("How many words do you want to generate: ")) # Get the amount of the words
filename = input("What will be the name of the file(leave blank to create no file): ") # Get the filename
findWord = input("What is the word to find after(leave blank if you don't want to search): ") # Get the word to find

###MAIN###

try: # Try this
    for pos in range(wordCount+1):  # Cycle through the the list of the wordCount
        currWord = "" # The variable for saving each letter to form a new "word"
        for i in range(wordLength): # Cycle through the list of the wordLength 
            currWord += random.choice(letters) # Add new letter to the currWord variable
        words.append(currWord) # Append the word into the list of all of the words
        print(f"{pos}/{wordCount}. Written {currWord} to the list") # Print the word written to the list and the count (current words / all words)
except (Exception and KeyboardInterrupt) as e: # Catch either the exceptin or the KeyboardInterrupt
    if filename: # If the filename variable is not blank, do the thing below
        if not e: # If got nothing in the exception
            print("Terminating and saving now...")
        else: # Else if not blank
            print(f"Saving current list and aborting. Cause: {e}")
        f = open(filename, "x") # Create a file with the name from the filename variable
        f = open(filename, "w") # Open it in write mode
        f.write(" ".join(words)) # Using .join, join all the words in the list with a space
        print(f"Saved to the file {filename}.")
        print("Terminating...")
        exit() # Exit the program
    else: # Else if the filename variable is blank
        if not e: # If exception is blank
            print("Terminating now...")
        else: # Else if it's not
            print(f"Terminating. Cause: {e}")
        exit() # Exit the program


try: # Try this 
    f = open(filename, "x") # Create a file
    f = open(filename, "w") # Open it in write mode
    f.write(" ".join(words)) # Write the words
except FileExistsError: # Handle the FileExistsError by suggesting to the user to make up a new name for the file
    print("Oops! A file with that name already exists!")
    filename = input("Enter a new name for the file: ") # Get the new name for the file
    f = open(filename, "x") # Create the new file
    f = open(filename, "w") # Open it in write mode
    f.write(" ".join(words)) # Write words

if findWord: # If findWord contains something in it
    count = 0 # Counter for the found words
    for word in words: # Cycle through the list of the words (not the file)
        if word == findWord: # If found the word
            count += 1 # Add a point to the counter
    print(f"Found {count} requested word(s)") # Notify user
print("Done!") # Notify user about the comletition of the program

# July 6th, 2023
# Updated on the 2:17pm, July 9th