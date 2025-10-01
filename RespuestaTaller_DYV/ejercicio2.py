import pandas as pd
import os

# Definición de la clase producto
class producto: 
    def __init__(self, id, nombre, precio, calificacion, stock):
        self.id = id
        self.nombre = nombre
        self.precio = float(precio) 
        self.calificacion = float(calificacion)
        self.stock = int(stock)
        
# Función para comparar productos según calificación y
def comparar_productos(p1, p2):
    if p1.calificacion != p2.calificacion:
        return p1.calificacion > p2.calificacion # La mayor calificacion primero
    return p1.precio < p2.precio # Si se presenta un empate, menor precio primero 

# Función para fusionar dos subarreglos ordenados
def merge (izquierda, derecha):
    print(f" Mezclando \nIzquierda: {[p.nombre for p in izquierda]}\nDerecha: {[p.nombre for p in derecha]}")
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if comparar_productos(izquierda[i], derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
            
    # Se agregan los elemtos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    print(f"Resultado mezcla: {[p.nombre for p in resultado]}\n")
    return resultado

# Función principal de Merge sort
def merge_sort(productos):
    print(f"Dividiendo: {[p.nombre for p in productos]} ")
    if len(productos) <= 1:
        return productos
    
    
    # Dividir el arreglo en dos mitades
    mitad = len(productos) // 2
    izquierda = productos[:mitad]
    derecha = productos[mitad:]
    
    # Rescursivamente ordenar las dos mitades
    izquierda = merge_sort(izquierda)
    derecha =  merge_sort(derecha)
    
    #Fucionar las mitades ordenadas
    return merge(izquierda, derecha)
    

#Función para leer el archivo usando la biblioteca pandas
def leer_productos(archivo):
    try:
        #Leer archivo
        df = pd.read_csv(archivo, encoding='utf-8')
        #verificar si las columnas son correctas
        columnas_requeridas = ['id', 'nombre', 'precio', 'calificacion', 'stock']
        if not all(col in df.columns for col in columnas_requeridas):
            raise KeyError (f"El archivo debe de contener las columnas: {columnas_requeridas}")
        
        #Convertir el DataFrame en una lista de objetos Producto
        productos = [
            producto(row['id'], row['nombre'], row['precio'], row['calificacion'], row['stock'])
            for _, row in df.iterrows()
        ]
        return productos
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró")
        return[]
    except ValueError as e:
        print(f"Error en los datos: {e}")
        return []
    
# Función para guardar los productos ordenados en un nuevo archivo
def guardar_productos_ordenados(productos, archivo_salida):
    # Convertir la lista de productos a un DataFrame
    df = pd.DataFrame([
        {'id': prod.id, 'nombre': prod.nombre, 'precio': prod.precio, 
         'calificacion': prod.calificacion, 'stock': prod.stock}
        for prod in productos
    ])
    # Guardar en CSV
    df.to_csv(archivo_salida, index=False, encoding='utf-8')
    print(f"Productos ordenados guardados en {archivo_salida}")

# Programa principal
def main():
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    archivo_entrada = os.path.join(directorio_script, 'productos.csv')
    archivo_salida = os.path.join(directorio_script, 'productos_ordenados.csv')
    
    # Leer productos del archivo
    productos = leer_productos(archivo_entrada)
    if not productos:
        return
    
    # Ordenar productos usando Merge Sort
    productos_ordenados = merge_sort(productos)
    
    # Guardar productos ordenados
    guardar_productos_ordenados(productos_ordenados, archivo_salida)
    
    if productos_ordenados:
        mejor_calif = productos_ordenados[0].calificacion
        mejores = [p for p in productos_ordenados if p.calificacion == mejor_calif]
        menor_precio = min (p.precio for p in mejores)
        mejores_final = [p for p in mejores if p.precio == menor_precio]
        
        
        print ("\n Mejores productos mayor calificacion y mejor precio (en caso de empate): )")
        for p in mejores_final:
            print (f"ID: {p.id}, NOMBRE: {p.nombre}, CALIFICACIÓN: {p.calificacion}, PRECIO: {p.precio}, STOCK: {p.stock}")
        

# Ejecutar el programa
if __name__ == "__main__":
    main()