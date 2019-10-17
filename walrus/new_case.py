numbers = []

print("Sum 'em all!")
print("Enter 0 to exit!")

while user_input := int(input('Please enter an integer: ')) != 0:
    numbers.append(user_input)

sum_ = sum(numbers)
print(sum_)
