secret_number = 7
while True:
    guess = int(input("Enter the single digit number to guess the secret number :"))

    if(guess == secret_number):
        print("Bullseye! You won")
        break
    elif(guess >= secret_number):
        print("tooo hight , try again")
    else:
        print("Toooo Low, Try agian")