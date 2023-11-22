# Importamos las bibliotecas necesarias
import socket
from tkinter import Tk, Entry, Button, messagebox, Label, StringVar

# Esta funcion envia datos al servidor
def enviar_datos(servidor_ip, servidor_puerto, datos, entry):
    if not datos:
        messagebox.showerror("Error", "No hay datos para enviar.")
        return

    # Creamos un socket de cliente
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente_socket.connect((servidor_ip, servidor_puerto))
        cliente_socket.sendall(datos.encode())
    except (ConnectionRefusedError, socket.gaierror, socket.timeout) as e:
        messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")
        return
    except socket.error as e:
        messagebox.showerror("Error", f"Error al enviar datos: {e}")
        return
    finally:
        cliente_socket.close()

    messagebox.showinfo("Éxito", "Datos enviados con éxito.")
    entry.delete(0, 'end')

# Esta funcion crea la interfaz de usuario del cliente
def crear_gui():
    window = Tk()
    window.title("Cliente")
    window.geometry("300x200")

    Label(window, text="Introduce los datos a enviar:").pack()
    entry_text = StringVar()
    entry = Entry(window, textvariable=entry_text, width=30)
    entry.pack()

    button = Button(window, text="Enviar datos", command=lambda: enviar_datos("localhost", 12345, entry_text.get(), entry))
    button.pack()

    window.mainloop()

if __name__ == "__main__":
    crear_gui()

"""
# Descripción del Archivo

Este archivo define un cliente simple que se conecta a un servidor, envía datos al servidor y luego cierra la conexión. Veamos qué hace cada parte:

- La función `enviar_datos` se utiliza para enviar datos al servidor. Esta función crea un socket de cliente, se conecta al servidor y envía los datos. Si ocurre algún error durante este proceso, se muestra un mensaje de error.

- La función `crear_gui` se utiliza para crear la interfaz de usuario del cliente. Crea una ventana con un campo de entrada para los datos a enviar y un botón para enviar los datos.

- Finalmente, si este archivo se ejecuta como el script principal, se llama a la función `crear_gui` para iniciar la interfaz de usuario.

Y eso es todo. ¡Espero que esto te ayude a entender mejor cómo funciona tu aplicación!

"""