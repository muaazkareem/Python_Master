numbers = [2, 5, 8, 11, 14, 17, 20, 23]
Even_numbers = []

for number in numbers:
    if number % 2 == 0:
        Even_numbers.append(number)
        
print(Even_numbers)