
    def invertir_lista(self, lista):
     
        inicio = 0
        fin = len(lista) - 1

      
        while inicio < fin:
        
            lista[inicio], lista[fin] = lista[fin], lista[inicio]
      
            inicio += 1
            fin -= 1

        return lista

data = Data()
lista_original = [1, 2, 3, 4, 5]
lista_invertida = data.invertir_lista(lista_original)
print(lista_invertida)  

pass
  def invertir_lista(self, lista):
        inicio = 0
        fin = len(lista) - 1
        while inicio < fin:
            lista[inicio], lista[fin] = lista[fin], lista[inicio]
            inicio += 1
            fin -= 1
        return lista

    def buscar_elemento(self, lista, elemento):
       
 
        for indice in range(len(lista)):

            if lista[indice] == elemento:
                return indice
  
        return -1


data = Data()
lista = [10, 20, 30, 40, 50]
elemento_buscado = 30
indice = data.buscar_elemento(lista, elemento_buscado)
print(indice) 

elemento_no_encontrado = 60
indice = data.buscar_elemento(lista, elemento_no_encontrado)
print(indice)  

pass

    def invertir_lista(self, lista):
        
        inicio = 0
        fin = len(lista) - 1
        while inicio < fin:
            lista[inicio], lista[fin] = lista[fin], lista[inicio]
            inicio += 1
            fin -= 1
        return lista

    def buscar_elemento(self, lista, elemento):
       
        for indice in range(len(lista)):
            if lista[indice] == elemento:
                return indice
        return -1

    def eliminar_duplicados(self, lista):
      
        lista_sin_duplicados = []
        for elemento in lista:
            if elemento not in lista_sin_duplicados:
                lista_sin_duplicados.append(elemento)
        return lista_sin_duplicados


data = Data()
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = data.eliminar_duplicados(lista_con_duplicados)
print(lista_sin_duplicados)  

pass

class data:
   
    def invertir_lista(self, lista):
      
        inicio = 0
        fin = len(lista) - 1
        while inicio < fin:
            lista[inicio], lista[fin] = lista[fin], lista[inicio]
            inicio += 1
            fin -= 1
        return lista

    def buscar_elemento(self, lista, elemento):
      
        for indice in range(len(lista)):
            if lista[indice] == elemento:
                return indice
        return -1

    def eliminar_duplicados(self, lista):
       
        lista_sin_duplicados = []
        for elemento in lista:
            if elemento not in lista_sin_duplicados:
                lista_sin_duplicados.append(elemento)
        return lista_sin_duplicados

    def merge_ordenado(self, lista1, lista2):
    
        lista_combinada = []
        i, j = 0, 0

    
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                lista_combinada.append(lista1[i])
                i += 1
            else:
                lista_combinada.append(lista2[j])
                j += 1


        while i < len(lista1):
            lista_combinada.append(lista1[i])
            i += 1


        while j < len(lista2):
            lista_combinada.append(lista2[j])
            j += 1

        return lista_combinada


data = Data()
lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
lista_combinada = data.merge_ordenado(lista1, lista2)
print(lista_combinada)

pass

def rotar_lista(lista, k):
   
    if not lista or k == 0:
        return lista

    
    k = k % len(lista)

    return lista[-k:] + lista[:-k]

lista = [1, 2, 3, 4, 5]
k = 2
print(rotar_lista(lista, k))  

pass

def encuentra_numero_faltante(lista):
   
   
    n = len(lista) + 1

 
    suma_esperada = n * (n + 1) // 2

    suma_actual = sum(lista)

 
    return suma_esperada - suma_actual


lista = [1, 2, 4, 5, 6]
print(encuentra_numero_faltante(lista))  

pass

def es_subconjunto(conjunto1, conjunto2):
   
 
    for elemento in conjunto1:
       
        if elemento not in conjunto2:
            return False
 
    return True


conjunto1 = [1, 2, 3]
conjunto2 = [1, 2, 3, 4, 5]
print(es_subconjunto(conjunto1, conjunto2))  

conjunto1 = [1, 2, 6]
conjunto2 = [1, 2, 3, 4, 5]
print(es_subconjunto(conjunto1, conjunto2))  

pass

class Pila:
    def __init__(self):
     
        self.items = []

    def push(self, item):
        
        self.items.append(item)

    def pop(self):
       El elemento superior de la pila, o None si la pila está vacía.
        
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
      
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        
     
        return len(self.items) == 0


pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
print(pila.peek())  
print(pila.pop())   
print(pila.is_empty())  
print(pila.pop())   
print(pila.pop())   
print(pila.is_empty())  


pass

class Cola:
    def __init__(self):
     
        self.items = []

    def enqueue(self, item):
       
        self.items.append(item)

    def dequeue(self):
      
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
       
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
       
        return len(self.items) == 0


cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(cola.peek())  # Salida: 1
print(cola.dequeue())  # Salida: 1
print(cola.is_empty())  # Salida: False
print(cola.dequeue())  # Salida: 2
print(cola.dequeue())  # Salida: 3
print(cola.is_empty())  # Salida: True

pass

def matriz_transpuesta(matriz):
   
    if not matriz or not matriz[0]:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = [[None] * filas for _ in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]

    return transpuesta

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz_transpuesta(matriz))

