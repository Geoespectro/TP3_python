# Importamos las bibliotecas necesarias
import socket
from tkinter import Tk, Entry, Button, messagebox, Label, StringVar
import threading

# Definimos una variable global para controlar si el servidor está en ejecucion
servidor_en_ejecucion = True

def iniciar_servidor(servidor_ip, servidor_puerto, label):
    global servidor_en_ejecucion
    servidor_en_ejecucion = True  
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor_socket.bind((servidor_ip, servidor_puerto))
    servidor_socket.listen(1)
    servidor_socket.settimeout(1)  
    print("Servidor iniciado. Esperando conexiones...")

    # Bucle principal del servidor
    while servidor_en_ejecucion:
        try:
            cliente_socket, cliente_direccion = servidor_socket.accept()
            print(f"Conexión aceptada de {cliente_direccion}.")
            datos = cliente_socket.recv(1024)
            datos_str = datos.decode()
            print(f"Datos recibidos: {datos_str}")
            label.config(text=f"Datos recibidos: {datos_str}")
            cliente_socket.close()

            # Registramos los datos recibidos en un archivo de registro
            with open('log_servidor.txt', 'a') as log_file:
                log_file.write(f"Datos recibidos de {cliente_direccion}: {datos_str}\n")

        except socket.timeout:
            continue  
        except socket.error as e:
            print(f"Error al aceptar conexión: {e}")

    servidor_socket.close()
    print("Servidor detenido.")

# Esta funcion detiene el servidor
def detener_servidor():
    global servidor_en_ejecucion
    servidor_en_ejecucion = False

# Esta funcion crea la interfaz de usuario del servidor
def crear_gui():
    window = Tk()
    window.title("Servidor")
    window.geometry("300x200")

    Label(window, text="Datos recibidos:").pack()
    label_text = StringVar()
    label = Label(window, textvariable=label_text, width=30)
    label.pack()

    button_iniciar = Button(window, text="Iniciar servidor", command=lambda: threading.Thread(target=iniciar_servidor, args=("localhost", 12345, label)).start())
    button_iniciar.pack()

    button_detener = Button(window, text="Detener servidor", command=detener_servidor)
    button_detener.pack()

    window.mainloop()

if __name__ == "__main__":
    crear_gui()

"""
# Descripción del Archivo

Este archivo define un servidor simple que acepta conexiones de clientes, recibe datos de los clientes, los imprime y los registra en un archivo de registro. Veamos qué hace cada parte:

- El servidor se inicia llamando a la función `iniciar_servidor`. Esta función crea un socket de servidor, lo vincula a la dirección IP y al puerto del servidor especificados, y luego comienza a escuchar las conexiones entrantes.

- Cuando se acepta una conexión de un cliente, el servidor recibe datos del cliente, los decodifica a una cadena y los imprime. También actualiza una etiqueta en la interfaz de usuario con los datos recibidos y registra los datos en un archivo de registro.

- La función `detener_servidor` se utiliza para detener el servidor. Simplemente cambia una variable global `servidor_en_ejecucion` a `False`, lo que hace que el bucle principal del servidor se detenga.

- La función `crear_gui` se utiliza para crear la interfaz de usuario del servidor. Crea una ventana con una etiqueta para mostrar los datos recibidos y dos botones para iniciar y detener el servidor.

- Finalmente, si este archivo se ejecuta como el script principal, se llama a la función `crear_gui` para iniciar la interfaz de usuario.

Y eso es todo. ¡Espero que esto te ayude a entender mejor cómo funciona tu aplicación!

"""