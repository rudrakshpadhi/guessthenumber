#guess the number
print('-----------GUESS THE NUMBER----------------')
print('\n'*5)
print('you get three tries to guess the single digit number')
import random 
l=[1,2,3,4,5,6,7,8,9]
number=random.choice(l)
tries=0
while tries<3:
    guess=int(input('enter a number between 0 and 10:\n'))
    if guess in range(0,10):
        if guess==number:
            print('you guessed the number, the number is',number)
            quit()
        elif tries==2:
            break
        elif guess!=number:
            print('wrong, you get another try')

        
    else:
        print('entered number is not between 0 and 10')
    tries=tries+1
print('the number was',number,'and your guess was',guess)



