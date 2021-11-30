import string

rights = 5
word = list(input("write a word for a little game : "))
guessword = list(len(word)*"_")
inWords = []
outWords = []
letter_list = list(string.ascii_lowercase)
mode = True #True in
result = ""

def inMode():
    global word,guessword,mode,letter,inWords
    print(f"Guessed word: {letter} You are IN mode")
    num = 0
    for i in word:
        if i == letter:
            guessword[num] = letter
        num += 1
    mode = True
    return(inWords.append(letter),guessword,mode)
    
def outMode():
    global rights,mode,letter,outWords
    print(f"Guessed word: {letter} You are OUT mode")
    rights -= 1
    mode = False
    return(outWords.append(letter),mode,rights)

while rights > 0:
    if guessword == word :
        result = "You won the game!"
        print(result)
        break
    else:
        print(f"You have {rights} guesses left")
        print(guessword)
        letter = input("guess a letter : ")
        if (letter in word) and (not letter in inWords):
            inMode()
        elif ((not letter in word) or (letter in inWords)) and mode:
            outMode()    
        elif (not letter in word) and (not letter in outWords) and (not mode):
            inMode()
        else:
            outMode()
if not result == "You won the game!":
    print("You lost the game")



