# Definimos la clase Observador, que se encarga de registrar las operaciones realizadas en la aplicacion.
class Observador:
    def __init__(self):
        pass

    # Este metodo registra una operacion de alta.
    def notificar_nueva_alta(self, identificacion, nomenclatura, tipo, fecha):
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"Operación de alta realizada con los siguientes detalles:\n")
            log_file.write(f"Identificación: {identificacion}\n")
            log_file.write(f"Nomenclatura: {nomenclatura}\n")
            log_file.write(f"Tipo: {tipo}\n")
            log_file.write(f"Fecha: {fecha}\n")
            log_file.write("\n")

    # Este metodo registra una operacion de baja.
    def notificar_baja(self, identificacion, nomenclatura, tipo, fecha):
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"Operación de baja realizada con los siguientes detalles:\n")
            log_file.write(f"Identificación: {identificacion}\n")
            log_file.write(f"Nomenclatura: {nomenclatura}\n")
            log_file.write(f"Tipo: {tipo}\n")
            log_file.write(f"Fecha: {fecha}\n")
            log_file.write("\n")

    # Este metodo registra una operacion de modificacion.
    def notificar_modificacion(self, identificacion, nomenclatura, tipo, fecha):
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"Operación de modificación realizada con los siguientes detalles:\n")
            log_file.write(f"Identificación: {identificacion}\n")
            log_file.write(f"Nomenclatura: {nomenclatura}\n")
            log_file.write(f"Tipo: {tipo}\n")
            log_file.write(f"Fecha: {fecha}\n")
            log_file.write("\n")

    # Este metodo registra una operacion de consulta.
    def notificar_consulta(self, identificacion, nomenclatura, tipo, fecha):
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"Operación de consulta realizada con los siguientes detalles:\n")
            log_file.write(f"Identificación: {identificacion}\n")
            log_file.write(f"Nomenclatura: {nomenclatura}\n")
            log_file.write(f"Tipo: {tipo}\n")
            log_file.write(f"Fecha: {fecha}\n")
            log_file.write("\n")

"""
# Descripción del Archivo

Este archivo define una clase `Observador` que se utiliza para registrar las operaciones realizadas en tu aplicación. Veamos qué hace cada parte:

- La clase `Observador` tiene un constructor que no hace nada en este momento.

- Dentro de la clase `Observador`, se definen varios métodos: `notificar_nueva_alta`, `notificar_baja`, `notificar_modificacion` y `notificar_consulta`. Cada uno de estos métodos registra una operación diferente.

- Cada método abre un archivo llamado 'log.txt' en modo de escritura y añade una entrada al archivo. Esta entrada incluye el tipo de operación realizada y los detalles de la operación, como la identificación, la nomenclatura, el tipo y la fecha.

- Por ejemplo, el método `notificar_nueva_alta` registra una operación de alta, `notificar_baja` registra una operación de baja, `notificar_modificacion` registra una operación de modificación, y `notificar_consulta` registra una operación de consulta.

Y eso es todo. ¡Espero que esto te ayude a entender mejor cómo funciona tu aplicación!
"""