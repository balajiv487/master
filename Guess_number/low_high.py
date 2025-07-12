from random import randint
print("Welcome to the Higher-Lower Game!")
rnum=randint(0,10)
no_guess=0
while True:

        g=input("Guess a number:")
        if g.isdigit():
            integer_number=int(g)
            print("You entered:", integer_number)
            if integer_number>rnum:
                print("higher")
            elif integer_number<rnum:
                print("lower")
            else:
                print(f"You win ! Your guess {g} is correct!")
                break
            no_guess +=1
        else:
            print("Invalid input. Please enter an integer number.")
