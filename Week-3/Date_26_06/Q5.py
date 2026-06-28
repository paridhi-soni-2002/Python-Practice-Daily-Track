numbers = [10,20,30,40,50]

try:

    index = int(input("Enter index: "))

    print(numbers[index])

except IndexError:

    print("Index out of range.")