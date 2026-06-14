#Number Guessing Game
secret_num=25
chance=5

while chance>0:
    
    num= int(input("enter any number you want to guess:"))
    if num==secret_num:
        print("you are correct:")
        break
    elif num>secret_num:
        print("guess less than value:")
       
    elif num<secret_num:
        print("guess a litte higher value:")
    chance-=1
       
    if chance==0:
        print("Time up you guess wrong") 
           
    
