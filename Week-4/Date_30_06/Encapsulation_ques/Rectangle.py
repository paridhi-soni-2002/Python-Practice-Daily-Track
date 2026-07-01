class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
        
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self,value):
        if value>0:
            self.__length=value
        else:
            print("length should not be -ve")
            

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if value>0:
            self.__width=value
        else:
            print("width could not be -ve")
            
    def area(self):
        area=self.__length*self.__width
        return area
    def perimeter(self):
        perimeter=2*(self.__length+self.__width)
        return perimeter
        

obj=Rectangle(10,20)
print(obj.area())
print(obj.perimeter()) 

