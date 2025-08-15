import random
image={'r':'🪨','p':'📃','s':'✂️'}
choices=('r','s','p')

while True:
    user_choice=input("Rock ,Paper, Scissor ? (r/p/s) : ")
    if user_choice not in choices:
        print("invalid choice")
        continue
    comp_choice=random.choice(choices)
    print(f'you chose {image[user_choice]}')
    print(f'computer chose {image[comp_choice]}')
    if user_choice==comp_choice:
        print("Its A Tie!!")
    elif user_choice=='r' and comp_choice=='s':
        print("Your the winner")
    elif user_choice=='s' and comp_choice=='p':
        print("you win")
    elif user_choice=='p' and comp_choice=='r':
        print("you win")
    else :
        print("you lose")
    a=input("do you want to continue (y/n)")
    if a=='n' or a=='N':
        break