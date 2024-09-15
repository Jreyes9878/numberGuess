import random

# Answer
answer = random.randint(0, 1000)
# print(answer) ## debug

# Initial Prompt
print('''Number Guessing Game:
A random number has been chosen, ranging from 0-1000
Guess numbers and get clues until you get it correct
----------------------------------------------------------------------------------------------''')

# Input loop
greater = 'Too High\n'
lower = 'Too Low\n'
input_list = []
while True:
    user_input = int(input("Guess a number: "))
    if user_input == answer:
        input_list.append(user_input)
        break
    elif user_input > answer:
        print(greater)
    else:
        print(lower)
    input_list.append(user_input)

# Player Won
print(f'''You have won!

It took {len(input_list)} attempts
Here are your guesses:
{input_list}

Fuck you!''')