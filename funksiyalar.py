import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters,word):
    display_letter=''
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += '_'
    return display_letter

def play():
    word =get_word()
    #so'zdagi harflar
    word_letters =set(word)
    #foydalanuvchi kiritgan harflar
    user_letters = ' '
    print(f"Мен {len(word)} хонали суз уйладим.Топа оласизми?")
    #print(word)
    while len(word_letters) > 0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f":Шу вактгача киритган харфларингиз:{user_letters}")

        letter = input("Харф киритинг: ").upper()
        if letter in word_letters:
            print("Бу харфларни аввал киритгансиз.Бошка харф киритинг")
            continue
        elif letter in word:
            word_letter.remove(letter)
            print(f"{letter} харфи тугри")
        else:
            print("Бундай харф йук.")
        user_letters += letter
    print(f"Табриклайман! {word} сузини {len(user_letters)} та уринишда топдингиз.")