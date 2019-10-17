numbers = []

print("Sum 'em all!")
print("Enter 0 to exit!")

user_input = int(input('Please enter an integer: '))

while user_input != 0:
    numbers.append(user_input)
    user_input = int(input('Please enter an integer: '))

sum_ = sum(numbers)
print(sum_)
