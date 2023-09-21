import random
tried = []

def input_letter():
    letter = str(input(f"Bitte geben Sie ein Bustabe abgesen von {tried} ein:")).upper()
    if len(letter) == 1 and letter not in tried:
        tried.append(letter)
        return letter
    else:
        return input_letter()


def choose_word():
    words = ["Hase", "Jazz", "Sags dir morgen"]
    rand = random.randint(0, len(words)-1)
    secret = words[rand].upper()
    hidden = ""
    for i in secret:
        hidden = hidden + "_"
    words = []
    words.append(secret)
    words.append(hidden)
    return words

def test_word(letter, secret, hidden):
    list_hidden = list(hidden)
    c = 0
    if letter in secret:
        for i in secret:
            if i == letter:
                list_hidden[c] = letter
            c += 1
        hidden = ""
        for i in list_hidden:
            hidden = hidden + i
        print(hidden)
    return hidden

def print_asci(error):
    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    if error >= 1:
        print(HANGMANPICS[error-1])



def hangman():
    print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ """)
    error = 0
    words = choose_word()
    secret = words[0]
    hidden = words[1]
    while error <= 7 and secret != hidden:
        letter = input_letter()
        hidden2 = test_word(letter, secret, hidden)
        if hidden2 == hidden:
            error += 1
        else:
            hidden = hidden2
        print_asci(error)
        print(hidden)

hangman()