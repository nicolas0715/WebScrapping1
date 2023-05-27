import csv

#Crear archivo txt con una sola lista de todos los productos
def txt1(fecha):
    # Abrir el archivo CSV en modo lectura
    with open('productos.csv', 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        
        # Abrir el archivo de texto en modo escritura
        with open('productos.txt', 'w') as archivo_txt:
            # Escribir los encabezados en el archivo de texto
            encabezados = ['Nombre', 'Precio', 'Precio Unitario', 'Precio Sugerido']
            archivo_txt.write('-' * int(((80 - len(fecha)) // 2)) + f' {fecha} ' + '-' * int(((80 - len(fecha)) // 2)) + '\n')
            archivo_txt.write('-' * 80 + '\n')
            linea_encabezados = f'{encabezados[0]:<30}{encabezados[1]:<15}{encabezados[2]:<18}{encabezados[3]:<15}'
            archivo_txt.write(linea_encabezados + '\n')
            archivo_txt.write('-' * 80 + '\n')
            
            # Escribir los datos en el archivo de texto
            for fila in lector_csv:
                nombre = fila['nombre']
                precio = fila['precio']
                precio_unitario = fila['precio_unitario']
                precio_sugerido = fila['precio_sugerido']
                
                linea = f'{nombre:<30}{precio:<15}{precio_unitario:<18}{precio_sugerido:<15}'
                archivo_txt.write(linea + '\n')

def txt2(l, lista, fecha):
    # Abrir el archivo CSV en modo lectura
    with open('productos.csv', 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        
        # Abrir el archivo de texto en modo escritura
        with open(f'prod_lista{l}.txt', 'w') as archivo_txt:
            # Escribir los encabezados en el archivo de texto
            encabezados = ['Nombre', 'Precio', 'Precio Unitario', 'Precio Sugerido']
            archivo_txt.write('-' * int(((80 - len(fecha)) // 2)) + f' {fecha} ' + '-' * int(((80 - len(fecha)) // 2)) + '\n')
            archivo_txt.write('-' * 80 + '\n')
            linea_encabezados = f'{encabezados[0]:<30}{encabezados[1]:<15}{encabezados[2]:<18}{encabezados[3]:<15}'
            archivo_txt.write(linea_encabezados + '\n')
            archivo_txt.write('-' * 80 + '\n')
            
            # Escribir los datos en el archivo de texto, pero solo de los archivos en la lista
            for fila in lector_csv:
                if fila['nombre'] in lista:
                    nombre = fila['nombre']
                    precio = fila['precio']
                    precio_unitario = fila['precio_unitario']
                    precio_sugerido = fila['precio_sugerido']
                    
                    linea = f'{nombre:<30}{precio:<15}{precio_unitario:<18}{precio_sugerido:<15}'
                    archivo_txt.write(linea + '\n')