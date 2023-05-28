
import random
def get_input():
    user_word = []
    user_input = input("please enter your words: ")
    while user_input != 'finish':
        if user_input.isalpha():
            user_word.append(user_input)
            user_input = input("please enter your word: ")

        else:
            user_input = input("please enter your word: ")

    return user_word
    print(user_word)



def random_choice(list):
    random_word = random.choice(list)
    return random_word




def get_input_to_choise_correct_word(list, number_of_gasses):

    correct_word = random_choice(list)
    
    for i in range(number_of_gasses):
        user_input = input("enter a word you gasse: ")
        if user_input == correct_word:
            print("congraguation you choice the correct word")
            return
        else:
            print("you choice the incorrect word!")
    print("you lose")



def information_of_game():
    print("welcome to the game")
    print("you should write several name")
    print("you should gasse the correct word in your word ")




information_of_game()
get_input_to_choise_correct_word(get_input(), 5)
