#Generate a random number and track how many times user tries to guess
import random


def guesser():
    print('Try to guess a random number between 1 and 15 will be generated for you')

    drawn = random.randint(1,15)
    counter = 0
    number_user = 0

    while True:
        number_user = input('Write: ')

        if number_user.isdigit():
            number_user = int(number_user)
            counter += 1
        else:
            print('Try number next time!')
            number_user = 0

        if drawn > number_user:
            print('Next time try a larger number than ', number_user)
        elif drawn < number_user:
            print('Next time try a smaller number than ', number_user)
        elif drawn == number_user:
            print('You did it! It took you', counter, 'tries')
            break

guesser()