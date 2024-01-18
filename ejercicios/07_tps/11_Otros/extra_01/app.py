import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

A) Al presionar el botón ‘Agregar' se debera cargar el nombre* y el precio** en sus respectivas listas.

* SOLO LETRAS MAYUSCULAS (A-Z)
** Enteros positivos

Si existe error al validar indicarlo mediante un Alert, cambiar el fondo del campo de texto con error
Si se cargo  coctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI AMBOS SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los articulos, sus precios y su posicion en la lista (por terminal)

C) Informar 
    1- Articulo mas caro
    2- Articulo mas barato
    3- Precio promedio
    4- Articulos que son mas caros que el promedio
    5- Articulos que son mas baratos que el promedio




'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_nombre_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Nombre Articulo")
        self.txt_nombre_articulo.grid(row=0, padx=20, pady=20)

        self.txt_precio_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.btn_agregar = customtkinter.CTkButton(
            master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(
            master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20,
                               columnspan=2, sticky="nsew")

        self.lista_nombre_articulo = ['TV', 'LICUADORA']
        self.lista_precio_articulo = [1000, 200]

    def btn_agregar_on_click(self):
        ingresarArticulo = self.txt_nombre_articulo.get()
        ingresarPrecio = self.txt_precio_articulo.get()
        if ingresarArticulo.isalpha() and ingresarArticulo.isupper() and ingresarPrecio.isdigit():
            self.lista_nombre_articulo.append(ingresarArticulo)
            self.lista_precio_articulo.append(ingresarPrecio)
            alert(title="titulo",message="El articulo y su precio se ingresaron perfectamente")
        elif ingresarArticulo.islower():
            self.txt_nombre_articulo.delete(0,25)
            self.txt_precio_articulo.delete(0,25)
            self.txt_nombre_articulo.insert(0,"Error")
            self.txt_precio_articulo.insert(0,"Error")
            alert(title="titulo", message="Ingreso el articulo en minuscula, todo en mayuscula por favor")
        elif not ingresarArticulo:
            self.txt_nombre_articulo.delete(0,25)
            self.txt_precio_articulo.delete(0,25)
            self.txt_nombre_articulo.insert(0,"Error")
            self.txt_precio_articulo.insert(0,"Error")
            alert(title="titulo", message="No ingreso nada en articulos")
        elif any(texto.isdigit() for texto in ingresarArticulo):
            self.txt_nombre_articulo.delete(0,25)
            self.txt_precio_articulo.delete(0,25)
            self.txt_nombre_articulo.insert(0,"Error")
            self.txt_precio_articulo.insert(0,"Error")
            alert(title="titulo",message="Ingreso un digito en vez de un texto en articulos")
        elif not ingresarPrecio:
            self.txt_nombre_articulo.delete(0,25)
            self.txt_precio_articulo.delete(0,25)
            self.txt_nombre_articulo.insert(0,"Error")
            self.txt_precio_articulo.insert(0,"Error")
            alert(title="titulo", message="No ingreso nada en precio")
        
        elif not ingresarPrecio.isdigit():
            self.txt_nombre_articulo.delete(0,25)
            self.txt_precio_articulo.delete(0,25)
            self.txt_nombre_articulo.insert(0,"Error")
            self.txt_precio_articulo.insert(0,"Error")
            alert(title="titulo", message="Ingreso un texto en vez de un digito en precio")
        else:
            ingresarPrecio = int(ingresarPrecio)
            if ingresarPrecio < 0:
                self.txt_nombre_articulo.delete(0,25)
                self.txt_precio_articulo.delete(0,25)
                self.txt_nombre_articulo.insert(0,"Error")
                self.txt_precio_articulo.insert(0,"Error")
                alert(title="titulo", message="Ingreso un precio menor a 0")

        pass

    def btn_mostrar_on_click(self):
        indices = []
        for indice ,valor in enumerate(self.lista_nombre_articulo):
            indices.append(indice) 
        print(self.lista_nombre_articulo, "\n" , self.lista_precio_articulo, "\n", indices)
        pass

    def btn_informar_on_click(self):

        listasUnidas = list(zip(self.lista_nombre_articulo, [int(x) for x in self.lista_precio_articulo]))
        articuloMasCaro = max(listasUnidas, key= lambda x: x[1])
        articuloMasBarato = min(listasUnidas, key= lambda x: x[1])
        promedioPrecios = sum([int(x) for x in self.lista_precio_articulo]) / len(self.lista_precio_articulo) 
        nombreMasCaroQuePromedio = []
        for clave, valor in listasUnidas:
            if valor > promedioPrecios:
                nombreMasCaroQuePromedio.append(clave)

        nombreMasBaratosQuePromedio = []
        for clave, valor in listasUnidas:
            if valor < promedioPrecios:
                nombreMasBaratosQuePromedio.append(clave)

        alert(title="titulo", message=f"El articulo mas caro es: {articuloMasCaro[0]} con un precio de {articuloMasCaro[1]} \nEl articulo mas barato es: {articuloMasBarato[0]} con un precio de {articuloMasBarato[1]}\nEl promedio de los precios ingresados es de: ${promedioPrecios}\nLos articulos que son mas caros que el promedio son: {nombreMasCaroQuePromedio} \nLos articulos que son mas baratos que el promedio son: {nombreMasBaratosQuePromedio}")

        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
