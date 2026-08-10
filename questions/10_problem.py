numbers = [12, 45, 7, 89, 34, 23, 67]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)