import random 
user_scor = 0
Ai_scor = 0
for _ in range(5):
    user_input = input("plese enter your choice between sang, kaghaz, gheychi: (s, k, gh)")

    user_choice = ['s', 'k', 'gh']
    ai_choice = random.choice(['k', 's', 'gh'])
    choice_dict = {
        's': 'sang',
        'k': 'kaghaz',
        'gh': 'gheychi'
    }
    if user_input in user_choice:
        print('\n', f'you enter {choice_dict[user_input]} and ai choice {choice_dict[ai_choice]}')
        if user_input == ai_choice:
            print('\n', "mosavi shodin dobare!")
            
        elif user_input == 's' and ai_choice == 'gh':
            print('\n', 'barande shodi')
            user_scor += 1
        elif user_input == 'k' and ai_choice == 's':
            print('\n', 'bande shodi')
            user_scor += 1
        elif user_input == 'gh' and ai_choice == 'k':
            print('\n', 'barande shodi')
            user_scor += 1
        else:
            print('\n', 'bakhti!')
            Ai_scor += 1
        print('\n',f"your scor is {user_scor} and AI scor is {Ai_scor}", '\n')
    else:
        print('your entery is incorrect!')
print('\n', '-' * 15, '\n')
if user_scor > Ai_scor:
    print(f"congratulation! you have {user_scor} and AI have {Ai_scor} so you was win", '\n')
elif user_scor == Ai_scor:
    print(f"Opss! you and AI was tie", '\n')
else:
    print(f"sorry! you hava {user_scor} and AI have {Ai_scor} so you was lose!", '\n')