import random

fruits = [1,2,3,4]
options = {'r' : '🪨' , 'p' : '📜📄', 's' :'✂️'}
choices = tuple(options.keys())

user_input = int(input("Select Option(1,2,3,4):"))

if (user_input == 1):
    guess = int(input("Guess a number from 1-10:"))
    guesser = random.randint(1,10)
    print(f"The random number is {guesser}")

if (user_input == 2):
    while True:
        choice = input("Enter R,P,S: ").lower()
        Ai = random.choice(choices)

        if (choice not in options):
            print("invalid input")
            continue

        result = print(f"Your choice is {options[choice]}  and Ai choice is {options[Ai]}")
        if(choice == 'r' and Ai == 's' or choice == 'p' and Ai == 'r' or choice == 's' and Ai == 'p'):
            print(f"you win {options[choice]}\nAi choice {options[Ai]}")
        elif (choice == 'r' and Ai == 'r' or choice == 'p' and Ai == 'p' or choice == 's' and Ai == 's'):
            print("It's a tie")
        else:
            print(f"you lose {options[choice]}\nAi choice {options[Ai]}")


        
        