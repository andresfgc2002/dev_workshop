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

pass

class NumberUtils:
    def es_numero_perfecto(self, n):
      
        if n <= 1:
            return False
        
        divisores = []
        for i in range(1, n):
            if n % i == 0:
                divisores.append(i)
        
        suma_divisores = sum(divisores)
        
        return suma_divisores == n


number_utils = NumberUtils()
print(number_utils.es_numero_perfecto(6))  
print(number_utils.es_numero_perfecto(28)) 
print(number_utils.es_numero_perfecto(10)) 

pass

class Matematicas:
    def triangulo_pascal(self, filas):
    
        triángulo = []
        
        for fila in range(filas):
            nueva_fila = [1] * (fila + 1)
            
          
            for j in range(1, fila):
                nueva_fila[j] = triángulo[fila - 1][j - 1] + triángulo[fila - 1][j]
            
            triángulo.append(nueva_fila)
        
        return triángulo


matematicas = Matematicas()
print(matematicas.triangulo_pascal(5))  

pass

class Matematicas:
    def factorial(self, n):
      
        if n == 0 or n == 1:
            return 1
        else:
            resultado = 1
            for i in range(2, n + 1):
                resultado *= i
            return resultado

matematicas = Matematicas()
print(matematicas.factorial(5)) 
print(matematicas.factorial(0))  

pass

class Matematicas:
    def mcd(self, a, b):
      
        while b != 0:
            a, b = b, a % b
        return a

matematicas = Matematicas()
print(matematicas.mcd(56, 98))  

