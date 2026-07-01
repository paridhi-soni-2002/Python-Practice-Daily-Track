class Banklocker:
    def __init__(self,lockno):
        self.__Lockerno=lockno
    @property
    def lockno(self):
        return self.__Lockerno
    
obj=Banklocker(1234)
print(obj.lockno)