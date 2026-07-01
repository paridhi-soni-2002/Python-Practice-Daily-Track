class University:
    def __init__(self,grade):
        self.__cgpa=grade
    @property
    def getgrade(self):
        return self.__cgpa
    @getgrade.setter
    def getgrade(self,value):
        if 0.0<value<=10.0:
            self.__cgpa=value
            return self.__cgpa
        else:
            print("invalid cgpa" )
            
obj=University(9.0)
print(obj.getgrade)
obj.getgrade=8.8
print(obj.getgrade)

        
