import random
def selectgame_level():
    user=input('Hi, enter your name here to begin:')
    print(f'Hello, {user} welcome to my number guessing game')
    game_level=int(input('Choose a game level here to start, 1 is for Easy, 2 is for Medium while 3 is for Hard:'))
    
    if game_level==1:
        def levelOne():
            print('Welcome to easy mode')
            number=random.randint(1,10)
            print('You have to guess between number 1 to 10')
            guesses=0
            while guesses<6:
                guess=int(input('Enter your guess here:'))
                guesses+=1
                guesses_left=6-guesses
                if guess==number:
                    print('You got it right!')
                    break
                else:
                    print('That was wrong')
                    print(f'You have {guesses_left} guesses left ')
       
            
            else:
                print('Game Over!')
        levelOne()

    elif game_level==2:
        def levelTwo():
            print('Welcome to medium mode')
            number=random.randint(1,20)
            print('You have to guess between number 1 to 20')
            guesses=0
            while guesses<4:
                guess=int(input('Enter your guess here:'))
                guesses+=1
                guesses_left=4-guesses
                if guess==number:
                    print('You got it right!')
                    break
                else:
                    print('That was wrong')
                    print(f'You have {guesses_left} guesses left ')
            else:
                print('Game Over!')

        levelTwo()
    elif game_level==3:
        def levelThree():
            print('Welcome to hard mode')
            number=random.randint(1,50)
            print('You have to guess between number 1 to 50')
            guesses=0
            while guesses<3:
                guess=int(input('Enter your guess here:'))
                guesses+=1
                guesses_left=3-guesses
                if guess==number:
                    print('You got it right!')
                    break
                else:
                    print('That was wrong')
                    print(f'You have {guesses_left} guesses left ')
            else:
                print('Game Over!')
        levelThree()

selectgame_level()
            

