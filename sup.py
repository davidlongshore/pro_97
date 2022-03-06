attempts = 5

print("attempts total: " + str(attempts))

print("chose a number between 1-9")
pocketMoney=int( input('enter a number: '))

number = 9

if(pocketMoney == number):
    print('number is correct. you win.')

if(pocketMoney < number):
    print('you aint got it')
    attempts = attempts - 1
    print('attempts left: ' + str(attempts))
    pocketMoney=int( input('enter a number: '))
    

if(attempts == 0):
    print("you lost. number is:" + str(number))