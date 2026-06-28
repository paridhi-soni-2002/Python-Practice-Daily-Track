try:
    filename=input("Enter file name:")
    file=open(filename,"r")
    print(file.read())
    file.close()
except FileNotFoundError:

    print("File not found.")   