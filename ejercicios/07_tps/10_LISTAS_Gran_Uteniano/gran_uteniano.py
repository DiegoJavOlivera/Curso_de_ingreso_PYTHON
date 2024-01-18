import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#? INTRODUCCION
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de 
los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está 
en la placa esta semana por haber ganado la inmunidad.

#! ENUNCIADO
Cada televidente que vota deberá ingresar:
* Nombre del votante
* Edad del votante (debe ser mayor a 13)
* Género del votante (Masculino, Femenino, Otro)
* El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario mediante alert:
    A) El promedio de edad de las votantes de género Femenino 
    B) Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
    C) Nombre del votante más joven qué votó a Gianni.
    D) Nombre de cada participante y porcentaje de los votos qué recibió.
    E) El nombre del participante que debe dejar la casa (El que tiene más votos)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Gran UTENIANO")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba
        # Cargar o modificar datos en estas listas
        self.lista_nombres = ["Pepe", "Moni","Paola","Coki", "Dardo", "Maria", "Fatiga"]
        self.lista_edades = [55, 45, 18, 17, 49, 45, 14]
        self.lista_genero = ["Masculino", "Femenino", "Otro"] 
        self.lista_participantes = ["Giovanni", "Gianni", "Facundo"]
        self.votantes = []

    def btn_cargar_on_click(self):
        
        while True:
            
            while True:
                ingresarNombre = prompt(title="titulo", prompt=f"Ingrese su nombre dentro de la lista {self.lista_nombres}").capitalize()
                if ingresarNombre is not None:
                    if ingresarNombre in ["Pepe", "Moni","Paola","Coki", "Dardo", "Maria", "Fatiga"]:
                        alert(title="titulo", message="El usuario a ingresado uno de los nombres seleccionado")
                        break
                    else:
                        alert(title="titulo", message="el usuario ingreso algo que no se encuentra en la lista")
                else:
                    alert(title="titulo",message="El usuario toco cancelar")
                    break
            while True:
                ingresarEdad = prompt(title="titulo", prompt=f"Ingrese su edad dentro de la lista {self.lista_edades}")
                if ingresarEdad is not None:
                    ingresarEdad = int(ingresarEdad)
                    if ingresarEdad in [55, 45, 18, 17, 49, 45, 14]:
                        alert(title="titulo",message="El usuario a ingresado una de las edades seleccionadas")
                        break
                    else:
                        alert(title="titulo", message="el usuario ingreso algo que no se encuentra en la lista")
                else:
                    alert(title="titulo",message="El usuario toco cancelar")
                    break
            while True:
                ingresarGenero = prompt(title="titulo", prompt=f"ingrese su genero dentro de esta lista: Masculino , Femenino, Otro").capitalize()
                if ingresarGenero is not None:
                    if ingresarGenero in ["Masculino", "Femenino", "Otro"] :
                        alert(title="titulo", message="El usuario a ingresado su genero")
                        break
                    else:
                        alert(title="titulo",message="El usuario a ingresado algo que no es valido")
                else:
                    alert(title="titulo",message="El usuario toco cancelar")
            while True:
                ingresarNombrePlaca = prompt(title="titulo", prompt=f"Ingresar el nombre del concursante en placa {self.lista_participantes}").capitalize()
                if ingresarNombrePlaca is not None:
                    if ingresarNombrePlaca in ["Giovanni", "Gianni", "Facundo"]:
                        alert(title="titulo", message=f"El usuario voto a {ingresarNombrePlaca}")
                        break
                    else:
                        alert(title="titulo", message="El usuario ingreso un nombre invalido")
                else:
                    alert(title="titulo",message="El usuario ingreso algo invalido")    
            
            self.votantes.append({"nombre": ingresarNombre, "edad":ingresarEdad, "genero":ingresarGenero, "voto":ingresarNombrePlaca})
            iniciar = prompt(title="titulo", prompt="Quieres continuar ? presiona 1 para si o 2 para no")
            iniciar = int(iniciar)
            if iniciar == 2:
                alert(title="titulo", message="El usuario no quiere continuar votando")
                break
            else:
                alert(title="titulo", message="El usuario ingreso 1, quiere seguir votando")
        pass
    def btn_mostrar_on_click(self):
        sumaFem = 0 
        contadorFem = 0
        for fem in self.votantes:
            if fem["genero"] == "Femenino":
                sumaFem += fem["edad"]
                contadorFem += 1
        premedioFem = sumaFem / contadorFem
        alert(title="titulo", message=f"El promedio de las votantes de genero Femenino es de {premedioFem}")

        cantidadMasVot_gia_facun = sum(1 for vot in self.votantes if vot["genero"] == "Masculino" and vot["edad"] > 25 and vot["edad"] < 40 and (vot["voto"] == "Giovanni" or vot["voto"] == "Facundo"))
        alert(title="titulo",message=f"La Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo es de {cantidadMasVot_gia_facun}")

        edad_mas_joven = float('inf')
        for nombre in self.votantes:
            if nombre["edad"] < edad_mas_joven and nombre["voto"] == "Giovanni":
                nombreMasJovenVot = nombre["nombre"]
                edad_mas_joven = nombre["edad"]
        if nombreMasJovenVot is not None:
            alert(title="titulo", message=f"El votante mas joven es {nombreMasJovenVot}")
        else:
            alert(title="titulo", message="No hay votante que haya votado a Giovanni")

        votosGiovanni = []
        cantidadVotantes = 0
        for votantes in self.votantes:
            cantidadVotantes += 1
            if votantes["voto"] == "Giovanni":
                votosGiovanni.append(votantes["nombre"])
        porcentajeGiovanni = (len(votosGiovanni)/cantidadVotantes) * 100

        votosFacundo = []
        for votantes in self.votantes:
            if votantes["voto"] == "Facundo":
                votosFacundo.append(votantes["nombre"])
        porcentajeFacundo = (len(votosFacundo) / cantidadVotantes) * 100

        votosGianni = []
        for votantes in self.votantes:
            if votantes["voto"] == "Gianni":
                votosGianni.append(votantes["nombre"])
        porcentajeGianni = (len(votosGianni) / cantidadVotantes) * 100

        alert(title="titulo", message=f"Cantidad de porcentaje: \nGiovanni: %{round(porcentajeGiovanni,2)}\nFacundo: %{round(porcentajeFacundo,2)}\nGianni: %{round(porcentajeGianni,2)}")

        votosGiovanniLen = len(votosGiovanni)
        votosFacundoLen = len(votosFacundo)
        votosGianniLen = len(votosGianni)
        if votosGiovanniLen > votosFacundoLen and votosGiovanniLen > votosGianniLen:
            alert(title="titulo", message=f"El participante mas votado es Giovanni con {votosGiovanniLen} votos")
        elif votosFacundoLen > votosGianniLen and votosFacundoLen > votosGiovanniLen:
            alert(title="titulo", message=f"El participante mas votados es Facundo con {votosFacundoLen} votos")
        elif votosGianniLen > votosFacundoLen and votosGianniLen > votosGiovanniLen:
            alert(title="titulo", message=f"El parcipante mas votado es Gianni con {votosGianniLen} votos")
        else:
            alert(title="titulo", message=f"Hay 2 o 3 con la misma cantidad de votos, Giovanni: {votosGiovanniLen}\nFacundo: {votosFacundoLen} \nGianni: {votosGianniLen}")


        pass
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()