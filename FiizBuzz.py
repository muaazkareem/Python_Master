# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If it is divisible by both 3 and 5, print "FizzBuzz".
# Otherwise, just print the number itself.

for i in range(1, 15 + 1):

    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i % 5 == 0):
        print("Buzz")
    elif(i % 3 == 0):
        print("Fizz")
    else:
        print(i)