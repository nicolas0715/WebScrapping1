import os
from git import Repo

def push():
    try:
        # Ruta local al repositorio
        repo_path = 'C:/Users/otero/Desktop/Pokio/Programacion/Proyectos/Proyectos_varios/Web_Scrapping1'

        # Pero para ejecutarlo con Actions, necesito la ruta local
        ruta_raiz = os.getcwd()

        # Inicializar el repositorio
        repo = Repo(ruta_raiz)

        # Agregar los archivos al repositorio (opcional)
        repo.index.add('productos.csv')

        # Commit con un mensaje
        repo.index.commit('Commit desde script')

        token = os.getenv('NICO_TOKEN')
        print(token)

        # Realizar el push al repositorio remoto
        origin = repo.remote('origin')
        origin_url = origin.url.replace('https://', f'https://token:{token}@') 
        origin.set_url(origin_url)
        origin.push()

    except Exception as e:
        print('El token es: ' + str(token))
        print('Error al realizar el push:', str(e)) 