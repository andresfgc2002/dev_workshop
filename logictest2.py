class Logica:


    def AND(self, a, b):
       
        return a and b

logica = Logica()
resultado = logica.AND(True, False)
print(resultado) 

pass

class Logica:
    
    def AND(self, a, b):
      
        return a and b

    def OR(self, a, b):
        de a OR b
        
        return a or b


logica = Logica()
resultado_and = logica.AND(True, False)
resultado_or = logica.OR(True, False)
print(resultado_and) 
print(resultado_or)  

pass

class Logica:
    

    def AND(self, a, b):
        
        return a and b

    def OR(self, a, b):
        
        return a or b

    def NOT(self, a):
      
        return not a


logica = Logica()
resultado_and = logica.AND(True, False)
resultado_or = logica.OR(True, False)
resultado_not = logica.NOT(True)
print(resultado_and)  
print(resultado_or)   
print(resultado_not)  

pass

class LogicOperations:
    def XOR(self, a, b):
        
        return (a or b) and not (a and b)

if __name__ == "__main__":
    logica = LogicOperations()

    print(logica.XOR(True, False))  
    print(logica.XOR(False, True))
    print(logica.XOR(True, True))   
    print(logica.XOR(False, False)) 

    pass

class LogicOperations:
    def XOR(self, a, b):
        
        return (a or b) and not (a and b)

    def NAND(self, a, b):
      
        return not (a and b)

if __name__ == "__main__":
    logica = LogicOperations()

    print(logica.XOR(True, False))  
    print(logica.XOR(False, True))  
    print(logica.XOR(True, True))   
    print(logica.XOR(False, False)) 

   
    print(logica.NAND(True, True))   
    print(logica.NAND(True, False))  
    print(logica.NAND(False, True))  
    print(logica.NAND(False, False)) 

pass

class LogicOperations:
    
    def NOR(self, a, b):
       
        return not (a or b)


if __name__ == "__main__":
    logica = LogicOperations()

    print(logica.NOR(True, True))   
    print(logica.NOR(True, False))  
    print(logica.NOR(False, True))  
    print(logica.NOR(False, False)) 

    pass

class LogicOperations:
    
    def XNOR(self, a, b):
        
        return not (a ^ b)


if __name__ == "__main__":
    logica = LogicOperations()

    print(logica.XNOR(True, True))  
    print(logica.XNOR(True, False))  
    print(logica.XNOR(False, True))  
    print(logica.XNOR(False, False)) 

pass

 def implicacion(self, a, b):
      
        return not a or b


if __name__ == "__main__":
    logica = LogicOperations()

     print(logica.implicacion(True, True))   
    print(logica.implicacion(True, False))  
    print(logica.implicacion(False, True))  
    print(logica.implicacion(False, False)) 



