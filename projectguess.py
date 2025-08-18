import random
number_to_guess=random.randint(1,100)
while True:
    try:
        guess=int(input("enter the number between 1 and 100 : "))
        if guess<number_to_guess:
            print("its too low")
        elif guess>number_to_guess:
            print("its too high")
        else:
            print("You have guessed the number")
            break
    except ValueError:
        print("enter the valid number")