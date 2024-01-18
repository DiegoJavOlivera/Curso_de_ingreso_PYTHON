import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Enunciado:

Una importante empresa dediada a la produccion de alfajores nos solicita una aplicacion que les 
permita controlar la produccion, dicha aplicacion contara con dos botones 

    - ALFAJOR ACEPTADO
    - ALFAJOR DESCARTADO

Mediante los cuales se registrara la cantidad total de alfajores producidos. 

Por tratarse de una produccion artesanal, cada alfajor puede variar su peso, por lo cual es importante
poder registrar el mismo al momento ACEPTARLO o DESCARTARLO. Los pesos deberan ser numeros flotantes 
positivos.

Receta en gramos:
Harina 000	         -   20
Almidón de Maíz	     -   5
Manteca	             -   10
Azúcar		         -   10
Cacao Amargo	     -   0.75
Polvo de hornear     -   0.5
Miel	             -   1
Extracto de Vainilla - 	 0.25
Huevo (gr)	         -   5
Dulce de Leche       -	 25


Al presionar el botón "Generar Informe" se deberá mostrar mediante alert 
la siguiente información:

	A - Cantidad total de alfajores fabricados
	B - Cantidad total de alfajores aceptados
	C - Cantidad total de alfajores rechazados
	D - Peso promedio de los alfajores aceptados
	E - Peso promedio de los alfajores rechazados

    F - Materia prima total utilizada *
    E - Materia prima total desperdiciada *

    *(Tener en cuenta que la cocion produce una merma de 15% del peso)


'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window

        self.title("UTN FRA")

        self.txt_label = customtkinter.CTkLabel(master=self, text="Peso estimado 61.84")
        self.txt_label.grid(row=0, padx= 0, pady= 0)

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="Peso Alfajor")
        self.txt_peso_articulo.grid(row=1, padx=0, pady=0)

        self.btn_aceptar = customtkinter.CTkButton(master=self, text="ACEPTAR", command=self.btn_aceptar_on_click)
        self.btn_aceptar.grid(row=2, pady=10, columnspan=2, sticky="news")

        self.btn_rechazar = customtkinter.CTkButton(master=self, text="RECHAZAR", command=self.btn_rechazar_on_click)
        self.btn_rechazar.grid(row=3, pady=10, columnspan=2, sticky="news")

        self.btn_generar_informe_notas = customtkinter.CTkButton(master=self, text="Generar Informe de Notas", command=self.btn_generar_informe_on_click)
        self.btn_generar_informe_notas.grid(row=5, pady=20, columnspan=2, sticky="news")
        
        self.lista_pesos_rechazados = []
        self.lista_pesos_aceptados = []
        self.ingredientes = {"harina 000":20, "almidon de maiz":5, "manteca":10, "azucar":10, "cacao amargo":0.75, "polvo para hornear": 0.5, "miel":1, "extracto de vainilla":0.25, "huevo":0.25, "dulce de leche":25}
    def btn_aceptar_on_click(self):
        peso = self.txt_peso_articulo.get()
        if any(valor.isalpha() for valor in peso):
            alert(title="titulo", message="El usuario a ingresado texto, solo debe ingresar numero")
        else:
            peso = float(peso)
            self.lista_pesos_aceptados.append(peso)
            alert(title="titulo",message="El usuario ingreso el peso del alfajor y fue ingresado a aceptados")
        pass
    
    def btn_rechazar_on_click(self):
        peso = self.txt_peso_articulo.get()
        if any(valor.isalpha() for valor in peso):
            alert(title="titulo", message="El usuario a ingresado texto, solo debe ingresar numero")
        else:
            peso = float(peso)
            self.lista_pesos_rechazados.append(peso)
            alert(title="titulo",message="El usuario ingreso el peso del alfajor y fue ingresado a rechazados")
        pass

    def btn_generar_informe_on_click(self):
        
        cantidadAlfaTotal = len(self.lista_pesos_aceptados) + len(self.lista_pesos_rechazados)
        cantidadTotalAceptado = len(self.lista_pesos_aceptados)
        cantidadTotalRechazados = len(self.lista_pesos_rechazados)
        sumaTotalIngredientes = sum(self.ingredientes.values()) - (sum(self.ingredientes.values()) * 0.15)
        promedioAceptados = sum(self.lista_pesos_aceptados) / len(self.lista_pesos_aceptados)
        promedioRechazados = sum(self.lista_pesos_rechazados) / len(self.lista_pesos_rechazados)
        materiaTotalUtilizada = {}
        for clave, valor in self.ingredientes.items():
            materiaTotalUtilizada[clave] = valor * (len(self.lista_pesos_aceptados) + len(self.lista_pesos_rechazados))
        materiaTotalDesperdiciada = {}
        for clave, valor in self.ingredientes.items():
            materiaTotalDesperdiciada[clave] = valor * len(self.lista_pesos_rechazados)

        alert(title="titulo", message=f"Los aljares aceptados tienen un peso total de: {round(sumaTotalIngredientes,2)} descontando la merma del %15 \n\nSe fabricaron un total de: {cantidadAlfaTotal} alfajores\n\nSe aceptaron una cantidad de: {cantidadTotalAceptado} alfajores\n\nSe rechazaron una cantidad de: {cantidadTotalRechazados} alfajores\n\nEl promedio del peso de los alfajores aceptado es de: {round(promedioAceptados,2)}\n\nEl promedio del peso de los alfajores rechazados es de: {round(promedioRechazados)}\n\nEl total de la materia prima utilizada en gramos es de: {materiaTotalUtilizada}\n\nEl total de la materia prima desperdiciada en gramos es de: {materiaTotalDesperdiciada}")
        


        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()    