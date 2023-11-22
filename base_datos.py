# Importamos las bibliotecas necesarias
import sqlite3
from peewee import Model, SqliteDatabase, CharField, DateField

# Creamos una instancia de 'SqliteDatabase'
db = SqliteDatabase('catalogo.db')

# Definimos una clase 'BaseModel'
class BaseModel(Model):
    class Meta:
        database = db

# Definimos un modelo 'Registro'
class Registro(BaseModel):
    identificacion = CharField(unique=True)
    nomenclatura = CharField(unique=True)
    tipo = CharField()
    fecha = DateField()

# Nos conectamos a la base de datos
db.connect()
db.create_tables([Registro])

"""
# Descripción del Archivo

Este archivo define una clase `Controller` que se utiliza para iniciar la aplicación. Aquí están los detalles:

- Importa las bibliotecas necesarias, incluyendo `tkinter`, `vista` y `observador`.

- La clase `Controller` se inicializa con un objeto `root` que es una instancia de `Tk` de `tkinter`. Esta instancia `root` se utiliza para crear la ventana principal de la aplicación.

- Dentro del constructor de `Controller`, se crea una instancia de `Ventana` (definida en el módulo `vista`) pasando el objeto `root` como argumento. Esta `Ventana` es la interfaz de usuario principal de la aplicación.

- También se crea una instancia de `Observador` (definida en el módulo `observador`). El propósito exacto de `Observador` depende de su implementación, pero generalmente se utiliza para manejar eventos o cambios de estado en la aplicación.

- Finalmente, si este archivo se ejecuta como el script principal (es decir, no se importa desde otro script), se crea una instancia de `Tk`, se pasa a una nueva instancia de `Controller`, y se inicia el bucle principal de `Tk` con `mainloop()`. Esto pone en marcha la aplicación y la mantiene en ejecución hasta que el usuario la cierre.
"""