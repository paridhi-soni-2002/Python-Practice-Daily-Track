class Patient:
    def __init__(self,blood_grp):
        self.__blood_group=blood_grp
        
    def get_blood_group(self):
        return self.__blood_group
    def set_blood_group(self,new_bg):
        if new_bg in "A+,B+,AB+,AB-,o+,o-":
         self.__blood_group=new_bg
         print("new blood group:",self.__blood_group)
        
obj=Patient("A+")
print(obj.set_blood_group("o+"))