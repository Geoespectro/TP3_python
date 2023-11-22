# Importamos las bibliotecas necesarias
import re
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import ttk
from base_datos import BaseModel, Registro
from validacion import Validacion
from observador import Observador

# Definimos un decorador para registrar las llamadas a las funciones de ABMC
def registro_log(func):
    def wrapper(*args, **kwargs):
        identificacion = args[1]
        if len(args) > 5:
            nomenclatura, tipo, fecha = args[2], args[3], args[4]
        else:
            nomenclatura, tipo, fecha = kwargs.get('nomenclatura'), kwargs.get('tipo'), kwargs.get('fecha')
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            print(f"Llamada a {func.__name__} con argumentos: Identificación: {identificacion}, Nomenclatura: {nomenclatura}, Tipo: {tipo}, Fecha: {fecha}\n")
        return func(*args, **kwargs)
    return wrapper

# Definimos la clase Abmc, que se encarga de realizar las operaciones de ABMC
class Abmc:
    def __init__(self):
        self.validacion = Validacion()
        self.observador = Observador()
        
    # Definimos la funcion de alta
    @registro_log
    def alta(self, identificacion, nomenclatura, tipo, fecha, tree):
        if (
            self.validacion.validar_identificacion(identificacion)
            and nomenclatura
            and tipo
            and fecha
        ):
            registro = Registro(
                identificacion=identificacion,
                nomenclatura=nomenclatura,
                tipo=tipo,
                fecha=fecha,
            )
            registro.save()
            self.observador.notificar_nueva_alta(identificacion, nomenclatura, tipo, fecha)
            messagebox.showinfo(
                "Alta Exitosa", f"El registro {identificacion} se ha dado de alta exitosamente."
            )
            self.actualizar_treeview(tree)

    # Definimos la funcion de baja
    @registro_log
    def baja(self, identificacion, nomenclatura, tipo, fecha, tree):
        item = tree.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un registro para dar de baja.")
            return

        identificacion, nomenclatura, tipo, fecha = tree.item(item, "values")

        confirmar = messagebox.askyesno(
            "Confirmación", f"¿Está seguro de borrar el registro {identificacion}?"
        )

        if confirmar:
            try:
                registro = Registro.get(Registro.identificacion == identificacion)
                registro.delete_instance()
                self.observador.notificar_baja(identificacion, nomenclatura, tipo, fecha)
                messagebox.showinfo(
                    "Baja Exitosa",
                    f"El registro {identificacion} ha sido borrado con éxito.",
                )
                self.actualizar_treeview(tree)
            except Registro.DoesNotExist:
                messagebox.showerror(
                    "Error",
                    f"No se encontró el registro con identificación {identificacion}.",
                )

    # Definimos la funcion de modificacion
    @registro_log
    def modificar(self, identificacion, nomenclatura, tipo, fecha, tree):
        item = tree.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un registro para modificar.")
            return

        identificacion_original = tree.item(item, "values")[0]

        nuevo_identificacion = identificacion
        nueva_nomenclatura = nomenclatura
        nuevo_tipo = tipo
        nueva_fecha = fecha

        if not nuevo_identificacion or not re.match(r"^\w{4,}$", nuevo_identificacion):
            messagebox.showerror(
                "Error al ingresar la identificación",
                "La identificación debe tener al menos 4 caracteres alfanuméricos.",
            )
            return

        try:
            registro = Registro.get(Registro.identificacion == identificacion_original)
            registro.identificacion = nuevo_identificacion
            registro.nomenclatura = nueva_nomenclatura
            registro.tipo = nuevo_tipo
            registro.fecha = nueva_fecha
            registro.save()
            self.observador.notificar_modificacion(
                nuevo_identificacion, nueva_nomenclatura, nuevo_tipo, nueva_fecha
            )
            messagebox.showinfo(
                "Modificación Exitosa", "El registro se ha modificado exitosamente."
            )
            self.actualizar_treeview(tree)
        except Registro.DoesNotExist:
            messagebox.showerror(
                "Error",
                f"No se encontró el registro con identificación {identificacion_original}.",
            )

    # Definimos la funcion de consulta
    @registro_log
    def consulta(self, identificacion, nomenclatura, tipo, fecha, tree):
        try:
            registro = Registro.get(Registro.identificacion ** f"{identificacion}")
            self.observador.notificar_consulta(registro.identificacion, registro.nomenclatura, registro.tipo, registro.fecha)
            messagebox.showinfo(
                "Registro Encontrado",
                f"Identificación: {registro.identificacion}\nNomenclatura: {registro.nomenclatura}\nTipo: {registro.tipo}\nFecha: {registro.fecha}",
            )
        except Registro.DoesNotExist:
            messagebox.showerror(
                "Error", f"No se encontró el registro con identificación {identificacion}."
            )

    # Esta funcion actualiza la tabla en la interfaz de usuario
    def actualizar_treeview(self, tree):
        tree.delete(*tree.get_children())
        registros = Registro.select()
        for registro in registros:
            tree.insert(
                "",
                "end",
                values=[
                    registro.identificacion,
                    registro.nomenclatura,
                    registro.tipo,
                    registro.fecha,
                ],
            )

"""
# Descripción del Archivo

Este archivo define una clase `Abmc` que se utiliza para realizar operaciones de alta, baja, modificación y consulta (ABMC) en tu aplicación. Veamos qué hace cada parte:

- La clase `Abmc` se inicializa con un objeto `Validacion` y un objeto `Observador`.

- La función `registro_log` es un decorador que se utiliza para registrar las llamadas a las funciones de ABMC.

- Las funciones `alta`, `baja`, `modificar` y `consultar` se utilizan para realizar las operaciones de ABMC. Cada una de estas funciones valida los datos de entrada, realiza la operación correspondiente en la base de datos y actualiza la tabla en la interfaz de usuario.

- La función `modificar` se utiliza para guardar los cambios realizados a un registro. Esta función obtiene el registro seleccionado en la tabla, actualiza los datos del registro con los nuevos datos y guarda los cambios en la base de datos.

- La función `consulta` se utiliza para realizar una consulta. Esta función obtiene los datos de los campos de entrada, busca el registro correspondiente en la base de datos y muestra los datos del registro.

- La función `actualizar_treeview` se utiliza para actualizar la tabla en la interfaz de usuario. Esta función borra todos los registros de la tabla, obtiene todos los registros de la base de datos e inserta los registros en la tabla.

Y eso es todo. ¡Espero que esto te ayude a entender mejor cómo funciona tu aplicación!
"""