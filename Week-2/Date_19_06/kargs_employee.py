def employee(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
        
employee(
    name="paridhi",
    age=23,
    city="Indore")