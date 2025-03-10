class FibonacciCalculator:
    def fibonacci(self, n):
    
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

fib_calculator = FibonacciCalculator()
print(fib_calculator.fibonacci(10))  

pass

class FibonacciCalculator:
    def secuencia_fibonacci(self, n):
       
        fibonacci_sequence = []
        a, b = 0, 1
        
        for _ in range(n):
            fibonacci_sequence.append(a)
            a, b = b, a + b
        
        return fibonacci_sequence

fib_calculator = FibonacciCalculator()
print(fib_calculator.secuencia_fibonacci(10))  

pass

class NumberUtils:
    def es_primo(self, n):
     
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

number_utils = NumberUtils()
print(number_utils.es_primo(7))  
print(number_utils.es_primo(10))  

pass

class NumberUtils:
    def es_primo(self, n):
     
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
       
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos


number_utils = NumberUtils()
print(number_utils.generar_primos(20)) 
