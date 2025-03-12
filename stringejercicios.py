class InversorDeCadenas:
    def invertir_cadena(self, texto):
        
        cadena_invertida = ""

        
        for i in range(len(texto) - 1, -1, -1):
            cadena_invertida += texto[i]

        return cadena_invertida


inversor = InversorDeCadenas()
texto_original = "Hola, mundo!"
texto_invertido = inversor.invertir_cadena(texto_original)
print(texto_invertido)  

pass

class ContadorDeVocales:
    def contar_vocales(self, texto):
       
        vocales = "aeiouAEIOU"
        contador = 0


        for caracter in texto:
            if caracter in vocales:
                contador += 1

        return contador

contador = ContadorDeVocales()
texto = "Hola, mundo!"
numero_de_vocales = contador.contar_vocales(texto)
print(numero_de_vocales)  

pass

class ContadorDeConsonantes:
    def contar_consonantes(self, texto):
      
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        contador = 0

    
        for caracter in texto:
            if caracter in consonantes:
                contador += 1

        return contador

contador = ContadorDeConsonantes()
texto = "Hola, mundo!"
numero_de_consonantes = contador.contar_consonantes(texto)
print(numero_de_consonantes)  

pass

class VerificadorDeAnagramas:
    def es_anagrama(self, texto1, texto2):
        
        texto1 = texto1.replace(" ", "").lower()
        texto2 = texto2.replace(" ", "").lower()

        if len(texto1) != len(texto2):
            return False

        frecuencia1 = {}
        frecuencia2 = {}

        for caracter in texto1:
            if caracter in frecuencia1:
                frecuencia1[caracter] += 1
            else:
                frecuencia1[caracter] = 1

        for caracter in texto2:
            if caracter in frecuencia2:
                frecuencia2[caracter] += 1
            else:
                frecuencia2[caracter] = 1

        return frecuencia1 == frecuencia2

verificador = VerificadorDeAnagramas()
texto1 = "Listen"
texto2 = "Silent"
es_anagrama = verificador.es_anagrama(texto1, texto2)
print(es_anagrama)  

pass

class ContadorDePalabras:
    def contar_palabras(self, texto):
    
        palabras = texto.split()

        return len(palabras)

contador = ContadorDePalabras()
texto = "Hola, mundo! Esto es una prueba."
numero_de_palabras = contador.contar_palabras(texto)
print(numero_de_palabras)

pass

class CapitalizadorDePalabras:
    def palabras_mayus(self, texto):
        
        palabras = texto.split()

        palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]

        texto_capitalizado = ' '.join(palabras_capitalizadas)

        return texto_capitalizado

capitalizador = CapitalizadorDePalabras()
texto = "el profesor es el mejor."
texto_capitalizado = capitalizador.palabras_mayus(texto)
print(texto_capitalizado)  

pass

import re

class ProcesadorTexto:
    def eliminar_espacios_duplicados(self, texto):
       
        return re.sub(r'\s+', ' ', texto).strip()

if __name__ == "__main__":
    procesador = ProcesadorTexto()
    
    texto = "camilo   le   gusta   el   pollo   con   curry."
    resultado = procesador.eliminar_espacios_duplicados(texto)
    
    print(f"Texto original: '{texto}'")
    print(f"Texto sin espacios duplicados: '{resultado}'")

pass

class CifradorCesar:
    def cifrar_cesar(self, texto, desplazamiento):

        resultado = []

        desplazamiento = desplazamiento % 26
        
        for caracter in texto:
            if 'a' <= caracter <= 'z': 
                nuevo_caracter = chr(((ord(caracter) - ord('a') + desplazamiento) % 26 + ord('a'))
                resultado.append(nuevo_caracter)
            elif 'A' <= caracter <= 'Z':  
                nuevo_caracter = chr(((ord(caracter) - ord('A') + desplazamiento) % 26 + ord('A'))
                resultado.append(nuevo_caracter)
            else:
              
                resultado.append(caracter)
        
        return ''.join(resultado)
if __name__ == "__main__":
    cifrador = CifradorCesar()
    
    texto = "Hola, Mundo!"
    desplazamiento = 3
    texto_cifrado = cifrador.cifrar_cesar(texto, desplazamiento)
    
    print(f"Texto original: '{texto}'")
    print(f"Texto cifrado (desplazamiento={desplazamiento}): '{texto_cifrado}'")

pass

class DescifradorCesar:
    def descifrar_cesar(self, texto, desplazamiento):
      
        resultado = []
        
        desplazamiento = desplazamiento % 26
        
        for caracter in texto:
            if 'a' <= caracter <= 'z':  
                nuevo_caracter = chr(((ord(caracter) - ord('a') - desplazamiento) % 26 + ord('a'))
                resultado.append(nuevo_caracter)
            elif 'A' <= caracter <= 'Z':  
         
                nuevo_caracter = chr(((ord(caracter) - ord('A') - desplazamiento) % 26 + ord('A'))
                resultado.append(nuevo_caracter)
            else:
                resultado.append(caracter)
        
        return ''.join(resultado)
if __name__ == "__main__":
    descifrador = DescifradorCesar()
    
    texto_cifrado = "Krod, Pxqgr!"
    desplazamiento = 3
    texto_descifrado = descifrador.descifrar_cesar(texto_cifrado, desplazamiento)
    
    print(f"Texto cifrado: '{texto_cifrado}'")
    print(f"Texto descifrado (desplazamiento={desplazamiento}): '{texto_descifrado}'")

    pass
    
    class BuscadorSubcadena:
    def encontrar_subcadena(self, texto, subcadena):
    
        posiciones = []
        longitud_texto = len(texto)
        longitud_subcadena = len(subcadena)
        
  
        if longitud_subcadena == 0:
            return posiciones
        
        for i in range(longitud_texto - longitud_subcadena + 1):
         
            if texto[i:i + longitud_subcadena] == subcadena:
                posiciones.append(i)
        
        return posiciones


if __name__ == "__main__":
    buscador = BuscadorSubcadena()
    
    texto = "abracadabra"
    subcadena = "abra"
    posiciones = buscador.encontrar_subcadena(texto, subcadena)
    
    print(f"Texto: '{texto}'")
    print(f"Subcadena: '{subcadena}'")
    print(f"Posiciones de la subcadena: {posiciones}")

pass




