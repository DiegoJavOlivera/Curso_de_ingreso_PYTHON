'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from collections import Counter
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
        postulantes = []
        ingresar_postulantes = prompt(title="titulo",prompt="Ingresar la cantidad de postulantes que va a ingresar hasta 10")
        ingresar_postulantes = int(ingresar_postulantes)
        for i in range(ingresar_postulantes):
            nombre = prompt(title="titulo",prompt="Ingresar nombre").capitalize()
            edad = prompt(title="titulo",prompt="Ingresar edad") 
            edad= int(edad)

            genero = prompt(title="titulo",prompt="Ingresar su genero (F-M-NB)").upper()
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt(title="titulo",prompt="Ingresar su genero (F-M-NB)").upper()

            tecnologia = prompt(title="titulo",prompt="seleccione un lenguaje (PYTHON - JS - NET)").upper()
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "NET":
                tecnologia = prompt(title="titulo",prompt="seleccione un lenguaje (PYTHON - JS - NET)").upper()

            puesto = prompt(title="titulo",prompt="Ingrese el puesto (JR - SSR - SR)").upper()
            while puesto != "JR" and puesto != "SSR" and puesto != "SR":
              puesto = prompt(title="titulo",prompt="Ingrese el puesto (JR - SSR - SR)").upper()

            postulantes.append({"nombre":nombre, "edad":edad, "genero":genero, "tecnologia":tecnologia, "puesto":puesto })

        cantidad_Nb_JS_NET = sum(1 for p in postulantes if p["genero"] == "NB" and p["edad"] > 25 and p["edad"] < 40 and p["puesto"] == "SSR" and p["tecnologia"] == "NET" or p["tecnologia"] == "JS"  )
        print(f"La cantidad de postulantes de genero no binario que programan en NET o JS que su edad rondan entre los 25 y 40 años de edad son: {cantidad_Nb_JS_NET}")

        for menor in postulantes:
            menor_edad = None
            if menor["edad"] < 25 and menor["puesto"] == "JR":
                menor_edad = menor["nombre"]
                break
        if menor_edad is not None:
            print(f"El postulante Junion menor de edad es {menor_edad}")
        else:
            print("No se encontro postulante menor de edad ")

        sumaFemenino = 0
        contadorFem = 0
        for f in postulantes:
            if f["genero"] == "F":
                sumaFemenino += f["edad"]
                contadorFem += 1
        PromedioFem = int(sumaFemenino / contadorFem)
        print(f"El promedio de edad de las postulantes femeninas es de: {PromedioFem}")
        porcentajeFem = (contadorFem / ingresar_postulantes) * 100 
        
        sumaMasculino = 0
        contadorMas = 0 

        for f in postulantes:
            if f["genero"] == "M":
                sumaMasculino += f["edad"]
                contadorMas +=1
        promedioMas = int(sumaMasculino / contadorMas)
        print(f"El promedio de edad de los postulantes masculinos es de: {promedioMas}")
        porcentajeMas = (contadorMas / ingresar_postulantes) * 100

        sumaNoBinario = 0 
        contadorNoBin = 0
        for f in postulantes:
            if f["genero"] == "NB":
                sumaNoBinario += f["edad"]
                contadorNoBin += 1
        promedioNoBin = int(sumaNoBinario / contadorNoBin)
        print(f"El promedio de edad de los postulantes no binarios es de: {promedioNoBin}")
        porcentajeNoBin = (contadorNoBin / ingresar_postulantes) * 100

        tecnologias = [persona["tecnologia"] for persona in postulantes]
        conteo_tecnologias = Counter(tecnologias)

        tec_mas_popu = conteo_tecnologias.most_common(1)[0][0]
        postuTec_masPopu = conteo_tecnologias.most_common(1)[0][1]
        print(f"La tecnologia con mas postulantes es: {tec_mas_popu} con una cantidad de: {postuTec_masPopu}")

        print(f"Del total de los postulantes el %{porcentajeFem} es Femenino\n Del total de los postulantes el %{porcentajeMas} es Masculino\n Del total de los postulantes el %{porcentajeNoBin} es No binario ")
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
