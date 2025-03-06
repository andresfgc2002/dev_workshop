import math

class Geometria:
    def area_circulo(self, radio):
      
        return math.pi * radio**2

geometria = Geometria()  
radio = 4.0
area = geometria.area_circulo(radio)
print(f"El área del círculo es: {area:.2f} unidades cuadradas")

pass

import math

class Geometria:
    def perimetro_circulo(self, radio):
       
        return 2 * math.pi * radio

geometria = Geometria()  
radio = 4.0
perimetro = geometria.perimetro_circulo(radio)
print(f"El perímetro del círculo es: {perimetro:.2f} unidades")

pass

class Geometria:
    def area_triangulo(self, base, altura):
      
        return 0.5 * base * altura

geometria = Geometria()  
base = 6.0
altura = 4.0
area = geometria.area_triangulo(base, altura)
print(f"El área del triángulo es: {area} unidades cuadradas")

pass 

class Geometria:
    def perimetro_triangulo(self, lado1, lado2, lado3):
       
        return lado1 + lado2 + lado3

geometria = Geometria()  
lado1 = 5.0
lado2 = 6.0
lado3 = 7.0
perimetro = geometria.perimetro_triangulo(lado1, lado2, lado3)
print(f"El perímetro del triángulo es: {perimetro} unidades")

pass

class Geometria:
    def es_triangulo_valido(self, lado1, lado2, lado3):
        
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
    
geometria = Geometria()  
lado1 = 5.0
lado2 = 6.0
lado3 = 7.0
es_valido = geometria.es_triangulo_valido(lado1, lado2, lado3)
print(f"¿Es un triángulo válido? {es_valido}")

pass

class Geometria:
    def area_trapecio(self, base_mayor, base_menor, altura):
       
        return 0.5 * (base_mayor + base_menor) * altura

geometria = Geometria()  
base_mayor = 8.0
base_menor = 5.0
altura = 4.0
area = geometria.area_trapecio(base_mayor, base_menor, altura)
print(f"El área del trapecio es: {area} unidades cuadradas")

pass

class Geometria:
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        
        return 0.5 * diagonal_mayor * diagonal_menor

geometria = Geometria() 
diagonal_mayor = 10.0
diagonal_menor = 6.0
area = geometria.area_rombo(diagonal_mayor, diagonal_menor)
print(f"El área del rombo es: {area} unidades cuadradas")

pass

class Geometria:
    def area_pentagono_regular(self, lado, apotema):
       
        perimetro = lado * 5
        return 0.5 * perimetro * apotema


geometria = Geometria()  
lado = 6.0
apotema = 4.0
area = geometria.area_pentagono_regular(lado, apotema)
print(f"El área del pentágono regular es: {area} unidades cuadradas")

pass

class Geometria:
    def perimetro_pentagono_regular(self, lado):
      
        return 5 * lado
    
geometria = Geometria()  
lado = 6.0
perimetro = geometria.perimetro_pentagono_regular(lado)
print(f"El perímetro del pentágono regular es: {perimetro} unidades")

pass

class Geometria:
    def area_hexagono_regular(self, lado, apotema):
       
        perimetro = 6 * lado  
        return 0.5 * perimetro * apotema

geometria = Geometria() 
lado = 4.0
apotema = 3.0
area = geometria.area_hexagono_regular(lado, apotema)
print(f"El área del hexágono regular es: {area} unidades cuadradas")

pass

class Geometria:
    def perimetro_hexagono_regular(self, lado):
       
        return 6 * lado  

geometria = Geometria()  
lado = 4.0
perimetro = geometria.perimetro_hexagono_regular(lado)
print(f"El perímetro del hexágono regular es: {perimetro} unidades")

pass

class Geometria:
    def volumen_cubo(self, lado):
       
        return lado ** 3  
geometria = Geometria()  
lado = 3.0
volumen = geometria.volumen_cubo(lado)
print(f"El volumen del cubo es: {volumen} unidades cúbicas")

pass

class Geometria:
    def area_superficie_cubo(self, lado):
       
        return 6 * (lado ** 2)  

geometria = Geometria()  
lado = 3.0
area = geometria.area_superficie_cubo(lado)
print(f"El área de la superficie del cubo es: {area} unidades cuadradas")

pass

import math

class Geometria:
    def volumen_esfera(self, radio):
     
        return (4/3) * math.pi * (radio ** 3)  

geometria = Geometria()  
radio = 5.0
volumen = geometria.volumen_esfera(radio)
print(f"El volumen de la esfera es: {volumen} unidades cúbicas")

pass

import math

class Geometria:
    def area_superficie_esfera(self, radio):
       
        return 4 * math.pi * (radio ** 2)  

geometria = Geometria()  
radio = 5.0
area = geometria.area_superficie_esfera(radio)
print(f"El área de la superficie de la esfera es: {area} unidades cuadradas")

pass

import math

class Geometria:
    def volumen_cilindro(self, radio, altura):
        """
        Calcula el volumen de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Volumen del cilindro
        """
        return math.pi * (radio ** 2) * altura  

geometria = Geometria()  
radio = 4.0
altura = 10.0
volumen = geometria.volumen_cilindro(radio, altura)
print(f"El volumen del cilindro es: {volumen} unidades cúbicas")

pass

import math

class Geometria:
    def area_superficie_cilindro(self, radio, altura):
       
        return 2 * math.pi * radio * (radio + altura)

geometria = Geometria()  
radio = 4.0
altura = 10.0
area = geometria.area_superficie_cilindro(radio, altura)
print(f"El área de la superficie del cilindro es: {area} unidades cuadradas")

pass

import math

class Geometria:
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

geometria = Geometria()  
x1, y1 = 1.0, 2.0
x2, y2 = 4.0, 6.0
distancia = geometria.distancia_entre_puntos(x1, y1, x2, y2)
print(f"La distancia entre los puntos es: {distancia} unidades")

pass

class Geometria:
    def punto_medio(self, x1, y1, x2, y2):
        
      
        punto_medio_x = (x1 + x2) / 2
        punto_medio_y = (y1 + y2) / 2
        return (punto_medio_x, punto_medio_y)


geometria = Geometria()  # Crear una instancia de la clase Geometria
x1, y1 = 1.0, 2.0
x2, y2 = 4.0, 6.0
punto_medio = geometria.punto_medio(x1, y1, x2, y2)
print(f"El punto medio entre los puntos es: {punto_medio}")

pass

class Geometria:
    def pendiente_recta(self, x1, y1, x2, y2):
       
        if x2 == x1:
            raise ValueError("La pendiente es indefinida (recta vertical) porque x1 == x2.")
        return (y2 - y1) / (x2 - x1)

geometria = Geometria()  
x1, y1 = 1.0, 2.0
x2, y2 = 4.0, 6.0
pendiente = geometria.pendiente_recta(x1, y1, x2, y2)
print(f"La pendiente de la recta es: {pendiente}")

pass

class Geometria:
    def ecuacion_recta(self, x1, y1, x2, y2):
       
        A = y1 - y2
        B = x2 - x1
        C = (x1 * y2) - (x2 * y1)
        
        return (A, B, C)

geometria = Geometria()  
x1, y1 = 1.0, 2.0
x2, y2 = 4.0, 6.0
coeficientes = geometria.ecuacion_recta(x1, y1, x2, y2)
print(f"Los coeficientes de la ecuación de la recta son: A = {coeficientes[0]}, B = {coeficientes[1]}, C = {coeficientes[2]}")

pass

class Geometria:
    def area_poligono_regular(self, num_lados, lado, apotema):
      
        area = (num_lados * lado * apotema) / 2
        return area
    
geometria = Geometria()  
num_lados = 6 
lado = 4.0  
apotema = 3.0  

area = geometria.area_poligono_regular(num_lados, lado, apotema)
print(f"El área del polígono regular es: {area} unidades cuadradas")

pass

class Geometria:
    def perimetro_poligono_regular(self, num_lados, lado):
       
        perimetro = num_lados * lado
        return perimetro

geometria = Geometria()  
num_lados = 6  
lado = 4.0  

perimetro = geometria.perimetro_poligono_regular(num_lados, lado)
print(f"El perímetro del polígono regular es: {perimetro} unidades")

pass














