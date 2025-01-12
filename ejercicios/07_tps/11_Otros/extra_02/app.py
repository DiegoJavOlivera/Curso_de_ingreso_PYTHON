import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Enunciado:

La UTN nos solicita la creación de una aplicación para obtener información 
estadistica de las evaluaciones.

1. Al presionar el botón "Ingresar notas", se deberá solicitar mediante prompt 
las notas del los alumn@s. 

	A - Se deberá repetir la solicitud hasta que el usuario haga clic en el botón  
    "Cancelar" del prompt
	B - Se deberá validar que la nota sea un numero entero entre el 0 y el 10.
	C - Las notas ingresadas se deberán ir guardando en una lista.

2. Al presionar el botón "Mostrar notas" debemos mostrar por la terminal el 
listado de las notas, primero indicando su posición en la lista y luego el 
valor de la nota. Con el siguiente formato:

        "1 - Nota: 8"
        "2 - Nota: 4"
        "3 - Nota: 10"
        ...

3. Al presionar el botón "Generar Informe" se deberá mostrar mediante alert 
la siguiente información:

	A - Nota mas baja
	B - Nota mas alta
	C - Promedio de todas las notas
	D - Cantidad de evaluaciones con nota 10
	E - En el caso que el promedio sea menor a 3, informar con la leyenda: "El promedio desaprobo"
	En el caso que el promedio sea mayor a 4: "El promedio aprobo"
	En el caso que el promedio sea mayor a 7: "El promedio promocionó"

	Para el punto E se deberá utilizar match.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_ingresar_notas = customtkinter.CTkButton(master=self, text="Ingresar Notas", command=self.btn_ingresar_notas_on_click)
        self.btn_ingresar_notas.grid(row=3, pady=20, columnspan=2, sticky="news")

        self.btn_mostrar_notas = customtkinter.CTkButton(master=self, text="Mostrar Notas", command=self.btn_mostrar_notas_on_click)
        self.btn_mostrar_notas.grid(row=4, pady=20, columnspan=2, sticky="news")
        
        self.btn_generar_informe_notas = customtkinter.CTkButton(master=self, text="Generar Informe de Notas", command=self.btn_generar_informe_notas_on_click)
        self.btn_generar_informe_notas.grid(row=5, pady=20, columnspan=2, sticky="news")
        self.lista_notas = []
            
    def btn_ingresar_notas_on_click(self):
        while True:
            solicitarNota = prompt(title="titulo", prompt="Ingrese las notas del 1 al 10")
            if solicitarNota is None:
                alert(title="titulo", message="El usuario cancelo el ingreso de notas")
                break
            elif solicitarNota.isalpha():
                alert(title="titulo", message="El usuario a ingresado un texto, intente nuevamente")
        
            if solicitarNota.isdigit() and int(solicitarNota) >= 1 and int(solicitarNota) <= 10:
                self.lista_notas.append(solicitarNota)
                alert(title="titulo", message="El usuario ingreso una nota a la lista")
            else:
                if any(notas.isalpha() for notas in solicitarNota):
                    alert(title="titulo",message="El usuario ingreso Numero con texto, vuelva a intentarlo")    
        pass
    
    def btn_generar_informe_notas_on_click(self):
        for indice, valor in enumerate(self.lista_notas):
            print(indice," - nota:", valor)
        pass
        
    def btn_mostrar_notas_on_click(self):
        notaMasBaja = min(self.lista_notas)
        notaMasAlta = max(self.lista_notas)
        promedioNotas = sum(self.lista_notas) / len(self.lista_notas)
        cantidadNotaAlta = sum(1 for nota in self.lista_notas if nota == 10 )
        alert(title="titulo",message=f"La nota mas bajas es: {notaMasBaja}\nLa nota mas alta es: {notaMasAlta}\nEl promedio de todas las notas es: {promedioNotas}")
        match promedioNotas:
            case 1|2|3:
                alert(title="titulo",message=f"El promedio desaprobo con un {promedioNotas}")
            case 4|5|6:
                alert(title="titulo",message=f"El promedio aprobo con un {promedioNotas}")
            case 7|8|9|10:
                alert(title="titulo",message=f"El promedio promociono con {promedioNotas}")
        pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()  
            