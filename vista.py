# Importamos las bibliotecas necesarias
from tkinter import StringVar, Entry, ttk, Label, Button, messagebox, Toplevel, Tk
from tkinter.ttk import Combobox
import socket
from modelo import Abmc
from estilos import Estilos
from observador import Observador
from tkinter import Tk, Entry, Button, messagebox, Label, StringVar
import socket

# Esta funcion envia datos al servidor
def enviar_datos(servidor_ip, servidor_puerto, datos):
    try:
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((servidor_ip, servidor_puerto))
        cliente_socket.sendall(datos.encode())
        cliente_socket.close()
        messagebox.showinfo("Éxito", "Datos enviados con éxito.")
    except socket.error as e:
        messagebox.showerror("Error", f"Error al enviar datos: {e}")

# Definimos la clase Ventana, que se encarga de crear la interfaz de usuario de la aplicacion.
class Ventana:
    def __init__(self, window):
        self.root = window
        self.root.title("App")
        self.style = ttk.Style()
        self.var_identificacion = StringVar()
        self.var_nomenclatura = StringVar()
        self.var_tipo = StringVar()
        self.var_fecha = StringVar() 
        self.objeto_base = Abmc()
        self.estilos = Estilos(self.root, self.style)
        self.observador = Observador()
        self.titulo = Label(
            self.root,
            text="Catalogo",
            font=("Arial", 14),
            bg="#1D7373",
            fg="white",
        )
        self.titulo.grid(row=0, columnspan=4, padx=10, pady=10, sticky="ew")
        self.label_identificacion = Label(self.root, text="Identificación")
        self.label_identificacion.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_identificacion = Entry(self.root, textvariable=self.var_identificacion, width=25)
        self.entry_identificacion.grid(row=1, column=1, padx=10, pady=10)
        self.label_nomenclatura = Label(self.root, text="Nomenclatura")
        self.label_nomenclatura.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_nomenclatura = Entry(self.root, textvariable=self.var_nomenclatura, width=25)
        self.entry_nomenclatura.grid(row=2, column=1, padx=10, pady=10)
        self.label_tipo = Label(self.root, text="Tipo")
        self.label_tipo.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_tipo = Entry(self.root, textvariable=self.var_tipo, width=25)
        self.entry_tipo.grid(row=3, column=1, padx=10, pady=10)
        self.label_fecha = Label(self.root, text="Fecha")
        self.label_fecha.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_fecha = Entry(self.root, textvariable=self.var_fecha, width=25)
        self.entry_fecha.grid(row=4, column=1, padx=10, pady=10)
        
        # Creamos los botones de la interfaz de usuario
        boton_cambiar_color = Button(
            self.root,
            text="Cambiar Color",
            bg="#1D7373",
            fg="white",
            command=self.cambiar_estilo,
            width=15,
        )
        boton_cambiar_color.grid(row=1, column=2, padx=10, pady=10)

        self.boton_alta = Button(
            self.root,
            text="Alta",
            bg="#1D7373",  
            fg="white",   
            command=self.alta,
            width=10,
        )
        self.boton_alta.grid(row=6, column=0, padx=10, pady=10)

        self.boton_borrar = Button(
            self.root,
            text="Borrar",
            bg="#1D7373",
            fg="white",
            command=self.borrar,
            width=10,
        )
        self.boton_borrar.grid(row=6, column=1, padx=10, pady=10)
        self.boton_modificar = Button(
            self.root,
            text="Modificar",
            bg="#1D7373",
            fg="white",
            command=self.abrir_modificar,
            width=10,
        )
        self.boton_modificar.grid(row=6, column=2, padx=10, pady=10)

        self.boton_consultar = Button(
            self.root,
            text="Consultar",
            bg="#1D7373",
            fg="white",
            command=self.abrir_consultar,
            width=10,
        )
        self.boton_consultar.grid(row=6, column=3, padx=10, pady=10)
        

        self.boton_enviar = Button(
        self.root,
        text="Enviar al servidor",
        bg="#1D7373",
        fg="white",
        command=self.enviar_al_servidor,
        width=15,
        )
        self.boton_enviar.grid(row=2, column=2, padx=10, pady=10)


        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("identificacion", "nomenclatura", "tipo", "fecha")
        self.tree.column("#0", width=0, stretch="no")
        self.tree.column("identificacion", width=100, anchor="w")
        self.tree.column("nomenclatura", width=100, anchor="w")
        self.tree.column("tipo", width=100, anchor="w")
        self.tree.column("fecha", width=100, anchor="w")
        self.tree.heading("#0", text="")
        self.tree.heading("identificacion", text="Identificación")
        self.tree.heading("nomenclatura", text="Nomenclatura")
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("fecha", text="Fecha")
        self.tree.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.actualizar()

    #Funcion de alta
    def alta(self):
        self.objeto_base.alta(
            self.var_identificacion.get(),
            self.var_nomenclatura.get(),
            self.var_tipo.get(),
            self.var_fecha.get(),
            self.tree,
        )
        self.clear_fields()
  
    #Funcion de borrar
    def borrar(self):
           
        seleccionado = self.tree.focus()
        if seleccionado:
            item = self.tree.item(seleccionado)
            valores = item["values"]
            if valores:
                    
                self.objeto_base.baja(valores[0], valores[1], valores[2], valores[3], self.tree)

    # Esta funcion abre una nueva ventana para modificar un registro
    def abrir_modificar(self):
        seleccionado = self.tree.focus()
        if seleccionado:
            item = self.tree.item(seleccionado)
            valores = item["values"]
            if valores:
                ventana_modificar = Toplevel(self.root)
                ventana_modificar.title("Modificar Registro")

                label_identificacion = Label(ventana_modificar, text="Identificación")
                label_identificacion.grid(row=0, column=0, padx=10, pady=10)
                entry_identificacion = Entry(ventana_modificar, textvariable=self.var_identificacion)
                entry_identificacion.grid(row=0, column=1, padx=10, pady=10)

                label_nomenclatura = Label(ventana_modificar, text="Nomenclatura")
                label_nomenclatura.grid(row=1, column=0, padx=10, pady=10)
                entry_nomenclatura = Entry(ventana_modificar, textvariable=self.var_nomenclatura)
                entry_nomenclatura.grid(row=1, column=1, padx=10, pady=10)

                label_tipo = Label(ventana_modificar, text="Tipo")
                label_tipo.grid(row=2, column=0, padx=10, pady=10)
                entry_tipo = Entry(ventana_modificar, textvariable=self.var_tipo)
                entry_tipo.grid(row=2, column=1, padx=10, pady=10)

                label_fecha = Label(ventana_modificar, text="Fecha")
                label_fecha.grid(row=3, column=0, padx=10, pady=10)
                entry_fecha = Entry(ventana_modificar, textvariable=self.var_fecha)
                entry_fecha.grid(row=3, column=1, padx=10, pady=10)

                entry_identificacion.insert(0, valores[0])
                entry_nomenclatura.insert(0, valores[1])
                entry_tipo.insert(0, valores[2])
                entry_fecha.insert(0, valores[3])

                boton_guardar = Button(
                    ventana_modificar,
                    text="Guardar Cambios",
                    bg="#1D7373",
                    fg="white",
                    command=lambda: self.guardar_modificacion(ventana_modificar),
                )
                boton_guardar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un registro para modificar.")

    # Esta funcion guarda los cambios realizados a un registro
    def guardar_modificacion(self, ventana_modificar):
        self.objeto_base.modificar(
            self.var_identificacion.get(),
            self.var_nomenclatura.get(),
            self.var_tipo.get(),
            self.var_fecha.get(),
            self.tree,
        )
        ventana_modificar.destroy()
        self.clear_fields()
        self.actualizar()
        messagebox.showinfo("Éxito", "Registro modificado con éxito.")

    # Esta funcion abre una nueva ventana para consultar un registro
    def abrir_consultar(self):
        ventana_consultar = Toplevel(self.root)
        ventana_consultar.title("Consultar Registro")

        label_consultar = Label(ventana_consultar, text="Ingrese la Identificación")
        label_consultar.grid(row=0, column=0, padx=10, pady=10)
        entry_consultar = Entry(ventana_consultar, textvariable=self.var_identificacion)
        entry_consultar.grid(row=0, column=1, padx=10, pady=10)

        # Creamos el boton para realizar la consulta
        boton_buscar = Button(
            ventana_consultar,
            text="Buscar",
            bg="#1D7373",
            fg="white",
            command=self.consultar,
        )
        boton_buscar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Esta funcion realiza la consulta
    def consultar(self):
        identificacion = self.var_identificacion.get()
        nomenclatura = self.var_nomenclatura.get()  
        tipo = self.var_tipo.get()  
        fecha = self.var_fecha.get()  
        self.objeto_base.consulta(identificacion, nomenclatura, tipo, fecha, self.tree)
        self.var_identificacion.set("")

    # Esta funcion limpia los campos de entrada
    def clear_fields(self):
        self.var_identificacion.set("")
        self.var_nomenclatura.set("")
        self.var_tipo.set("")
        self.var_fecha.set("")

    # Esta funcion actualiza la tabla en la interfaz de usuario
    def actualizar(self):
        self.objeto_base.actualizar_treeview(self.tree)

    # Esta funcion cambia el estilo de la interfaz de usuario
    def cambiar_estilo(self):
        self.estilos.cambiar_estilo()
        self.root.configure

    # Esta funcion envía los datos de un registro seleccionado al servidor
    def enviar_al_servidor(self):
        item = self.tree.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un registro para enviar.")
            return

        datos = self.tree.item(item, "values")
        datos_str = ",".join(str(dato) for dato in datos)

        if not datos_str:
            messagebox.showerror("Error", "No hay datos para enviar.")
            return

        try:
            cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente_socket.connect(("localhost", 12345))
            cliente_socket.sendall(datos_str.encode())
        except (ConnectionRefusedError, socket.gaierror, socket.timeout) as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")
        except socket.error as e:
            messagebox.showerror("Error", f"Error al enviar datos: {e}")
        else:
            messagebox.showinfo("Éxito", "Datos enviados con éxito.")
        finally:
            cliente_socket.close()


if __name__ == "__main__":
    root_tk = Tk()
    application = Ventana(root_tk)
    application.actualizar()
    root_tk.mainloop()

"""
# Descripción del Archivo

Este archivo define una clase `Ventana` que se utiliza para crear la interfaz de usuario de tu aplicación. Veamos qué hace cada parte:

- La clase `Ventana` se inicializa con una ventana `window`. Dentro del constructor, se configura el título de la ventana y se crean varios widgets, incluyendo etiquetas, campos de entrada y botones.

- Los campos de entrada se utilizan para recoger los datos del usuario, como la identificación, la nomenclatura, el tipo y la fecha.

- Los botones se utilizan para realizar varias acciones, como cambiar el estilo de la interfaz de usuario, dar de alta, borrar y modificar.

- La función `enviar_datos` se utiliza para enviar datos al servidor. Esta función crea un socket de cliente, se conecta al servidor y envía los datos. Si ocurre algún error durante este proceso, se muestra un mensaje de error.

- La función `abrir_modificar` se utiliza para abrir una nueva ventana que permite al usuario modificar un registro existente. Esta función obtiene el registro seleccionado en la tabla, llena los campos de entrada con los datos del registro y muestra un botón para guardar los cambios.

- La función `guardar_modificacion` se utiliza para guardar los cambios realizados a un registro. Esta función llama al método `modificar` del objeto `objeto_base`, cierra la ventana de modificación, limpia los campos de entrada y actualiza la tabla.

- La función `abrir_consultar` se utiliza para abrir una nueva ventana que permite al usuario consultar un registro existente. Esta función crea una nueva ventana con un campo de entrada para la identificación y un botón para realizar la consulta.

- La función `consultar` se utiliza para realizar la consulta. Esta función obtiene los datos de los campos de entrada, llama al método `consulta` del objeto `objeto_base` y limpia el campo de identificación.

- La función `clear_fields` se utiliza para limpiar los campos de entrada.

- La función `actualizar` se utiliza para actualizar la tabla en la interfaz de usuario. Esta función llama al método `actualizar_treeview` del objeto `objeto_base`.

- La función `cambiar_estilo` se utiliza para cambiar el estilo de la interfaz de usuario. Esta función llama al método `cambiar_estilo` del objeto `estilos`.

- La función `enviar_al_servidor` se utiliza para enviar los datos de un registro seleccionado al servidor. Esta función obtiene el registro seleccionado, convierte los datos a una cadena, y luego envía la cadena al servidor.

- Finalmente, si este archivo se ejecuta como el script principal, se crea una instancia de `Ventana`, se actualiza la tabla y se inicia el bucle principal de la interfaz de usuario.

Y eso es todo. ¡Espero que esto te ayude a entender mejor cómo funciona tu aplicación!
"""