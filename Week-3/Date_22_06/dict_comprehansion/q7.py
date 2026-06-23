# 29.	Create a dictionary mapping numbers from 1 to 10 to "Even" or "Odd".
even_odd={n:( "Even" if n%2==0 else "Odd") for n in range(1,51)
        }
print(even_odd)