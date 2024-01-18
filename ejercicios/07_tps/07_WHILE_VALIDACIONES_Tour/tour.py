
import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

"""
Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:


1 - nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y 
        su género es xxx"
2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
        medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.
3- Validar todos los datos.
4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. 
        Se pueden hacer desde 0 excursiones a 11 excursiones.
5- Una vez ingresada la cantidad se debe pedir por cada excursión 
        el importe y el tipo de excursión (caminata  o vehículo). 
        informar cual es el precio más caro, el más barato y el promedio
6- Informar cual es el tipo de excursión (caminata  o vehículo) 
        más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)
"""
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
    
    def btn_mostrar_on_click(self):
        a_pie = []
        en_auto = []
        solicitar_nombre = prompt(title="titulo",prompt="Ingresar su nombre")
        solicitar_edad = prompt(title="titulo",prompt="Ingrese su edad")
        solicitar_edad = int(solicitar_edad)
        solicitar_genero = prompt(title="titulo",prompt="Ingrese su genero")
        alert(title="titulo",message=f"usted es {solicitar_nombre}, usted tiene {solicitar_edad} de edad y su genero es {solicitar_genero}")
        solicitar_altura = prompt(title="titulo",prompt="Ingrese su altura en cm")
        solicitar_altura = int(solicitar_altura)
        if solicitar_altura < 140:
            alert(title="titulo",message=f"El cliente es menor a 140cm mide {solicitar_altura}")
        elif solicitar_altura > 140 and solicitar_altura < 170:
            alert(title="titulo",message=f"El cliente tiene una altura media de {solicitar_altura}")
        elif solicitar_altura > 170 and solicitar_altura < 190:
            alert(title="titulo",message=f"El cliente es alto, mide {solicitar_altura}cm")
        elif solicitar_altura > 190:
            alert(title="titulo",message=f"El cliente es muy alto, mide {solicitar_altura}cm")
        cantidad_excurciones = prompt(title="titulo",prompt="Ingresar la cantidad de excurciones que quiere realizar entre 0 y 11")
        cantidad_excurciones = int(cantidad_excurciones)
        contador = 0 
        while contador < cantidad_excurciones:
            solicitar_excurcion = prompt(title="titulo",prompt=f"Ingrese Caminata o Auto segun como quiera realizar la excurcion\nLleva {contador} excurciones seleccionadas").strip().capitalize()
            if solicitar_excurcion == "Caminata":
                alert(title="titulo",message="A ingresado Caminata")
                solicitar_costo = prompt(title="titulo",prompt="Ingrese el costo de la excurcion a Caminata")
                solicitar_costo = int(solicitar_costo)
                a_pie.append({"tipo":solicitar_excurcion, "costo":solicitar_costo})
                
                contador += 1
            elif solicitar_excurcion == "Auto":
                alert(title="titulo",message="A ingresado auto")
                solicitar_costo = prompt(title="titulo", prompt="Ingrese el costo de la excurcion en auto")
                solicitar_costo = int(solicitar_costo)
                en_auto.append({"tipo":solicitar_excurcion,"costo":solicitar_costo})
                contador += 1
            
        costoMaxCaminata = max(diccionario["costo"] for diccionario in a_pie if diccionario["tipo"] == "Caminata")
        costoMinCaminata = min(diccionario["costo"] for diccionario in a_pie if diccionario["tipo"] == "Caminata")
        PromedioCaminata = sum(diccionario["costo"] for diccionario in a_pie if diccionario["tipo"] == "Caminata") / len(a_pie)
        costoMaxAuto = max(diccionario["costo"] for diccionario in en_auto if diccionario["tipo"] == "Auto")
        costoMinAuto = min(diccionario["costo"] for diccionario in en_auto if diccionario["tipo"] == "Auto")
        promedioAuto = sum(diccionario["costo"] for diccionario in en_auto if diccionario["tipo"] == "Auto") / len(en_auto)

        alert(title="titulo",message=f"El costo mas caro en Caminata es de {costoMaxCaminata} \nEl costo minimo en Caminata es de {costoMinCaminata}\nEl promedio del costo en caminata es de {PromedioCaminata}\n\nEl costo mas caro en Auto es de {costoMaxAuto}\nEl costo minimo en Auto es de {costoMinAuto}\nEl promedio del costo en Auto es de {promedioAuto}")
        
        if len(a_pie) > len(en_auto):
            alert(title="titulo",message=f"Se selecciono Caminata una cantidad de: {len(a_pie)} veces")
        elif len(en_auto) > len(a_pie):
            alert(title="titulo",message=f"se selecciono en Auto una cantidad de: {len(en_auto)} veces")
        elif len(en_auto) == len(a_pie):
            alert(title="titulo",message=f"Se selecciono las mismas cantidad de veces en Auto y Caminata: {(len(a_pie))} veces")

        
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()