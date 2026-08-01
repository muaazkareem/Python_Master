
def Tickect_discounter():
    age = int(input("Enter your age to get disconted tickets : "))
    if(age <= 12):
        print("CONGRATS! You will get the discount, The ticket price for you is 500 rupee, Enjoy the movie!")
    elif(age >= 65):
        print("CONGRATS! You will get the discount, The ticket price for you is 700 rupee, Enjoy the movie!")
    else:
        print("You will get the ticket for 1000 rupees , Thank you !")
        
Tickect_discounter()