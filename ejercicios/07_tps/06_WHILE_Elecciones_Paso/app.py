'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

''' 
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        candidatos = []
        edades = {}
        while True:
            solicitar_nombre = prompt(title="titulo", prompt="ingrese el nombre del candidato que quiere votar")
            if solicitar_nombre is None:
                break
            candidato = solicitar_nombre.lower().capitalize()
            candidatos.append(candidato)
            while True:
                solicitar_edad = prompt(title="titulo", prompt="Ingrese la edad mayor a 25")
                if solicitar_edad.isdigit() and int(solicitar_edad) >= 25:
                    edad = int(solicitar_edad)
                    edades[candidato] = edad
                    break
        contadorMax_nombres = max(set(candidatos), key=candidatos.count)
        max_nombre = candidatos.count(contadorMax_nombres)
        contadorMin_nombre = min(set(candidatos),key=candidatos.count)
        
        edad_candidato_menos_votos = edades.get(contadorMin_nombre,None)
        
        promedio_edad = sum(edades.values()) / len(edades) if len(edades) > 0 else 0
        total_votos = len(candidatos)
        print(f"El candidato con mas votos es {contadorMax_nombres} con {max_nombre} \n El candidato con menos votos es {contadorMin_nombre} con {edad_candidato_menos_votos} años de edad.\nEl promedio de edad es de {promedio_edad}\n El total de votos emitidos es de {total_votos}")


        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
