# Importamos las bibliotecas necesarias
class Estilos:
    def __init__(self, root, style):
        self.root = root
        self.indice_estilo = 0
        
    def cambiar_estilo(self):
        temas = ["uno", "dos", "tres"]  

        # Si ya hemos aplicado un estilo, pasamos al siguiente.
        if self.indice_estilo:
            self.indice_estilo = (self.indice_estilo + 1) % len(temas)
        else:
            self.root.configure

        # Obtenemos el estilo actual.
        estilo_actual = temas[self.indice_estilo]

        # Dependiendo del estilo actual, cambiamos el color de fondo de la ventana principal.
        if estilo_actual == "uno":
            self.root.configure(bg="#A6BC09")
            
        elif estilo_actual == "dos":
            self.root.configure(bg="#CCEA8D")
            
        elif estilo_actual == "tres":
            self.root.configure(bg="#019587")

"""
# Descripción del Archivo

Este archivo define una clase `Estilos` que se utiliza para cambiar el estilo de la interfaz de usuario de tu aplicación. Veamos qué hace cada parte:

- La clase `Estilos` se inicializa con un objeto `root` y un `style`. El objeto `root` es una instancia de `Tk` de `tkinter` que representa la ventana principal de la aplicación. El `style` es una cadena que representa el estilo actual de la interfaz de usuario.

- Dentro de la clase `Estilos`, se define un método `cambiar_estilo`. Este método cambia el estilo de la interfaz de usuario al siguiente estilo disponible.

- Los estilos disponibles son "uno", "dos" y "tres". Cada estilo corresponde a un color de fondo diferente para la ventana principal de la aplicación.

- El método `cambiar_estilo` utiliza el atributo `indice_estilo` para llevar la cuenta del estilo actual. Cada vez que se llama a `cambiar_estilo`, `indice_estilo` se incrementa en 1 (o vuelve a 0 si ya ha alcanzado el número total de estilos disponibles).

- Dependiendo del valor de `indice_estilo`, se configura el color de fondo de la ventana principal a un color diferente.

Y eso es todo. ¡Espero que esto te ayude a entender mejor cómo funciona tu aplicación!

"""

