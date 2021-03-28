import random 

camputer_number = random.randint(0,20)

user_number = -1

while camputer_number != user_number:

    user_number = int(input())

    if camputer_number == user_number:
        print('tnx')

    elif camputer_number > user_number:
        print('go up')

    elif camputer_number <  user_number:
        print('go down')

print(int(user_number))