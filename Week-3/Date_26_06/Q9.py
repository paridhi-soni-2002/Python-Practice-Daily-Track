def add(a,b):

    try:

        print(a + b)

    except TypeError:

        print("Incompatible data types")


add(10,20)

add(10,"Python")