class AlphabetCycle:
    def __init__(self):
        self.index=0
        self.alphabet="abcdefghijklmnopqrstuvwxyz"
        
    def __iter__(self):
        return self
    def __next__(self):
      
       value=self.alphabet[self.index]
       self.index+=1
       if self.index==26:
           self.index=0
       return value




obj = AlphabetCycle()

for _ in range(100):
    print(next(obj))