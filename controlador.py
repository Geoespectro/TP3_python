# Este archivo que lanza nuestra aplicación
from tkinter import Tk
import vista
from observador import Observador

# Definimos una clase llamada 'Controller'
class Controller:
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = vista.Ventana(self.root_controler)
        self.observador = Observador()

if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)
    application.objeto_vista.actualizar()
    root_tk.mainloop()
  

"""
# Descripción del Archivo

Este archivo define una clase `Controller` que se utiliza para iniciar la aplicación. Aquí están los detalles:

- Importa las bibliotecas necesarias, incluyendo `tkinter`, `vista` y `observador`.

- La clase `Controller` se inicializa con un objeto `root` que es una instancia de `Tk` de `tkinter`. Esta instancia `root` se utiliza para crear la ventana principal de la aplicación.

- Dentro del constructor de `Controller`, se crea una instancia de `Ventana` (definida en el módulo `vista`) pasando el objeto `root` como argumento. Esta `Ventana` es la interfaz de usuario principal de la aplicación.

- También se crea una instancia de `Observador` (definida en el módulo `observador`). El propósito exacto de `Observador` depende de su implementación, pero generalmente se utiliza para manejar eventos o cambios de estado en la aplicación.

- Finalmente, si este archivo se ejecuta como el script principal (es decir, no se importa desde otro script), se crea una instancia de `Tk`, se pasa a una nueva instancia de `Controller`, y se inicia el bucle principal de `Tk` con `mainloop()`. Esto pone en marcha la aplicación y la mantiene en ejecución hasta que el usuario la cierre.

"""