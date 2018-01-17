def main():
    #Alphabetically sort the inital anagram
    anagram = sorted(input("Enter anagram: "))
    with open('dictionary.txt') as dictionary:
        #Go through each word in the dictionary file
        for current_word in dictionary:
            #Strip newline chars and alphabetically sort the current word
            current_word = current_word.rstrip()
            sorted_word = sorted(current_word)
            #If the current word sorted alphabetically matches the anagram
            #sorted alphabetically we know that the word is a solution for the anagram
            if(sorted_word == anagram):
                print(current_word)

if __name__ == "__main__":
   main()
