class ATM:

    def __init__(self, pin):
        self.__pin = pin

    def verify_pin(self, pin):

        if pin == self.__pin:
            print("Correct PIN")
        else:
            print("Wrong PIN")

    def change_pin(self, new_pin):

        if len(str(new_pin)) == 4:
            self.__pin = new_pin
            print("PIN Changed")
        else:
            print("PIN must be 4 digits")


obj = ATM(1234)

obj.verify_pin(1234)

obj.change_pin(5678)