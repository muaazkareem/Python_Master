guests = ["muaaz", "irfan", "ali", "abdullah", "ahmad", "hassan", "laika", "arwish"]

name = input("Enter your name please: ").strip().lower()

for guest in guests:
    if (name == guest):
        if len(guest) <= 5:
            print(f"We warmly welcome our VIP guest {guest.title()}!")
        else:
            print(f"Welcome, {guest.title()}!")
        break
else:
    print("Sorry, your name is not on the guest list.")