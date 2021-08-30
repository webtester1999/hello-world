import random

r = random.randrange(1,9)
total_turns = 0
correct_guessed  = 0
print('welcome to the guess game ,if your done with the game you can quit it by typing number more than 10')

while True:
    user = input('guess the number between 1 to 9 :')

    if r == int(user) :
        print('The user guessed exactly right')
        total_turns +=1
        correct_guessed = 1
    elif r > int(user) <10 :
        print('The user guessed too low')
        total_turns +=1
        correct_guessed = 0
    elif r < int(user) < 10:
        print('the user guessed too high')
        total_turns +=1
        correct_guessed = 0
    else:
        break
print(f'''The user total guesses are {total_turns}
            and correctly guessed are {correct_guessed}''' )
