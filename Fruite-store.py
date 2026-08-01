stock = {
    "apple": 150,
    "banana": 80,
    "milk": 210,
    "bread": 120
}
item = input("Enter What you want : ").strip().lower()
if item in stock:
    print(f"Yes {item.title()} is avalible for rupees {stock[item]} rupees. ")
else:
    print(f"Sorry! {item.title()} is not avalible now. ")
