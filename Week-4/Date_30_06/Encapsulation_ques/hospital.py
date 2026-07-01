class Hospital:

    def __init__(self, doctor, room):
        self.__doctor_name = doctor
        self.__room_number = room

    def admit(self):
        print("Patient Admitted")

    def discharge(self):
        print("Patient Discharged")

    def get_details(self):
        print(self.__doctor_name)
        print(self.__room_number)


obj = Hospital("Dr Sharma", 201)

obj.admit()

obj.get_details()