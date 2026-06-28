class InvalidAgeError(Exception):

    pass


try:

    age = int(input("Enter age: "))

    if age < 18:

        raise InvalidAgeError("Age must be at least 18.")

    print("Eligible")

except InvalidAgeError as e:

    print(e)