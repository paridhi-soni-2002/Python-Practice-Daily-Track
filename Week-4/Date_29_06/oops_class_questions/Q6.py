class Patient:

    def __init__(self, patient_id, name, age,
                 gender, disease, doctor_name,
                 room_number, blood_group):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.doctor_name = doctor_name
        self.room_number = room_number
        self.blood_group = blood_group

    def checkup(self):
        print(self.name, "is under checkup.")

    def admit(self):
        print(self.name, "has been admitted.")

    def discharge(self):
        print(self.name, "has been discharged.")

    def take_medicine(self):
        print(self.name, "is taking medicine.")

    def show_report(self):
        print("\nPatient:", self.name)
        print("Disease:", self.disease)
        print("Doctor :", self.doctor_name)
        print("Room   :", self.room_number)


patient = Patient(
    101,
    "Rahul",
    25,
    "Male",
    "Fever",
    "Dr. Sharma",
    201,
    "O+"
)

patient.admit()
patient.checkup()
patient.take_medicine()
patient.show_report()
patient.discharge()