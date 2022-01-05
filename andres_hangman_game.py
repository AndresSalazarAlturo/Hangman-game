import random
import os

filepath="./archivos/data.txt"

def game():

    with open(filepath, "r", encoding="utf-8") as f:
        
        words = []
        for word in f:
            words.append(word.strip().upper())

    my_word = random.choice(words)
    my_word_spaces = [letter for letter in my_word]
    my_word_spaces_underscores = ["_"] * len(my_word)
    word_dict = {}

    for key, value in enumerate(my_word):
        if not word_dict.get(value):
            word_dict[value] = []
        word_dict[value].append(key)

    while (True):
        os.system("cls")
        print("¡Guess the word!")

        for under_score in my_word_spaces_underscores:
            print(under_score + " ", end = "")
        print("\n")
        
        letter = input("Try any letter \n").strip().upper()
        assert letter.isalpha(), "Just letters please"

        if letter in my_word_spaces:
            for key in word_dict[letter]:
                my_word_spaces_underscores[key] = letter
        
        if "_" not in my_word_spaces_underscores:
            os.system("cls") 
            print("¡You won! The word was ", my_word)
            break

if __name__ == '__main__':
    game()