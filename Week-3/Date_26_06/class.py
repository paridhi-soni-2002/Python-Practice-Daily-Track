#exception handling
#exception- disturn the normal flow of program
#exception handling- exception handling is a mechanism used to handle
#runtime error so that program does not crash unexpected
#try= the code that may generate an exception is written inside try
#
# try:
#     num= int (input("enter number:"))
#     x=100/num
#     print(x)
# except ZeroDivisionError:
#     print("cannot divide by zero")
    
# #try,except,else,finally

# #except valueError:
# # print()

# #except ZeroDivisionError
# #finally block always execute no matter what happens

# #cleanup operations- 

# file=None
# try:
#     file=open("data.txt")
#     file.write()
#     file.close()
    
# except FileNotFoundError:
#     file.close()
#     print("file not found")
    
# finally:
#     if file:
#         file.close()
        
#     print("Flie closed")
    
#built in exceptions
# ValueError: wrong Value
# TypeError: wrong datatype
# NameError: variable not found
# IndexError: invalid Index
# KeyError: invalid dictionary Key
# ZeroDivisionError:divide by Zero
# FileNotFoundError
# ImportError
# PermissionError
# RuntimeError
# MemoryError

try:
    dict1={
        "abc":123,12:234
        }
    print(dict1["xyz"])
    
except KeyError as e:
    print("wrong value",e)
    
#custom exceptions: we can create own exception by inherting from exception

class AgeError(Exception):
    pass

try:
 age=23
 if age<18:
    raise AgeError("age must be atleast 10")

# print("Eligible")
except AgeError as e:
       print("error:",e)
       

#heirahcy exception
#BaseException-it is inherit into the exception
#exceptions:
#ArithematicError: ZeroDivisionError,OverflowError
#valueError:
#TypeError:
#RuntimeError:
#ImportError:ModuleNotFoundError
#FileNotFoundError

