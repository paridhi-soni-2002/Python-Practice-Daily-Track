# 9.	Implement memoization for the Fibonacci sequence using closures.
def fibonacci():
    memory={}
    def fib(n):
        if n in memory:
            return memory[n]
        if n<=1:
            return n
        memory[n]= fib(n-1)+fib(n-2)
        return memory
    return fib

obj=fibonacci()
print(obj(4))
