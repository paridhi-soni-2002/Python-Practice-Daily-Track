class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self):

        print("Function Started")

        self.func()

        print("Function Ended")


@Decorator
def greet():
    print("Hello")


greet()