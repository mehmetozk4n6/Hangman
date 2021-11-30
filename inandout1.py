import string

rights = 5
word = list(input("write a word for a little game : "))
guessword = list(len(word)*"_")
inWords = []
outWords = []
letter_list = list(string.ascii_lowercase)
mode = True #True in


while rights > 0:
    if guessword == word :
        print("You won the game!")
        break
    else:
        print(f"You have {rights} guesses left")
        print(guessword)
        letter = input("guess a letter : ")
        if (letter in word) and (not letter in inWords):
            print(f"Guessed word: {letter} You are IN mode")
            mode = True
            inWords.append(letter)
            num = 0
            for i in word:
                if i == letter:
                    guessword[num] = letter
                num += 1
        else:
            if ((not letter in word) or (letter in inWords)) and mode:
                print(f"Guessed word: {letter} You are OUT mode")
                outWords.append(letter)
                mode = False
                rights -= 1
            else:
                if (not letter in word) and (not letter in outWords) and (not mode):
                    print(f"Guessed word: {letter} You are IN mode")
                    mode = True
                    inWords.append(letter)
                    num = 0
                    for i in word:
                        if i == letter:
                            guessword[num] = letter
                    num += 1
                else:
                    print(f"Guessed word: {letter} You are OUT mode")
                    outWords.append(letter)
                    mode = False
                    rights -= 1

print("You lost the game")



