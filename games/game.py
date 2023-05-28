import random 

user_input = input("plese enter your choice between sang, kaghaz, gheychi: (s, k, gh)")

user_choice = ['s', 'k', 'gh']
ai_choice = random.choice(['k', 's', 'gh'])
choice_dict = {
    's': 'sang',
    'k': 'kaghaz',
    'gh': 'gheychi'
}
if user_input in user_choice:
    print(f'you enter {choice_dict[user_input]} and ai choice {choice_dict[ai_choice]}')
    if user_input == ai_choice:
        print("mosavi shodin dobare!")
    elif user_input == 's' and ai_choice == 'gh':
        print('barande shodi')
    elif user_input == 'k' and ai_choice == 's':
        print('bande shodi')
    elif user_input == 'gh' and ai_choice == 'k':
        print('barande shodi')
    else:
        print('you are lose!')
else:
    print('your entery is incorrect!')
