
limit = int(input("Enter the limit for average : "))
def average():
    if(limit == 3):
        num1 = int(input("Enter the First number :"))
        num2 = int(input("Enter the Second number :"))
        num3 = int(input("Enter the Third number :"))
        avg = (num1 + num2 + num3) / 3
        print(f"The average of the numbers is :{avg}")
    elif(limit == 2):
        num1 = int(input("Enter the First number :"))
        num2 = int(input("Enter the Second number :"))
        avg = (num1 + num2) / 2
        print(f"The average of the two numbers is : {avg}")
    else:
        print("Please enter more than 1 number less then 4. Thank You! ")

average()
