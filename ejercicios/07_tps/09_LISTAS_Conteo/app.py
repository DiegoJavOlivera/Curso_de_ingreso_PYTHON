import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

nivel A:
    i. el listado de numeros pares
    j. que se ingreso mas ?, positivos , negativos o ceros

nivel Ninja:
    k. el listado de los numeros mayores , si es que hay mas de un mayor

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista_numeros = []

    def btn_comenzar_ingreso_on_click(self):
        while True:
            ingresar_numero = prompt(title="titulo",prompt="Ingresar numeros")
            
            if ingresar_numero is not None:
                ingresar_numero = int(ingresar_numero)
                self.lista_numeros.append(ingresar_numero)    
                
            else:
                alert(title="titulo",message="No se ingreso ningun valor ")
                break
        pass

    def btn_mostrar_estadisticas_on_click(self):
        numeros_negativos = 0
        for numero in self.lista_numeros:
            if numero < 0:
                numeros_negativos += numero

        numeros_positivos = 0
        for numero in self.lista_numeros:
            if numero > 0:
                numeros_positivos += numero
        
        cantidad_negativos = 0
        for numero in self.lista_numeros:
            if numero < 0:
                cantidad_negativos += 1

        cantidad_positivos = 0
        for numero in self.lista_numeros:
            if numero > 0:
                cantidad_positivos += 1
        cantidad_ceros = sum(str(cero).count("0") for cero in self.lista_numeros)

        num_mas_neg = min(self.lista_numeros)
        num_max_pos = max(self.lista_numeros)

        contador = 0
        sumarnegativos = 0
        for promNum in self.lista_numeros:
            if promNum < 0:
                sumarnegativos += promNum
                contador += 1

        promedioNumNegativo = sumarnegativos / contador

        numerosPares = []
        cantidadPar = 0
        for numPar in self.lista_numeros:
            if numPar % 2 == 0: 
                cantidadPar += 1
                numerosPares.append(numPar)

        contadorPositivos = 0
        contadorNegativo = 0

        for selector in self.lista_numeros:
            if selector < 0:
                contadorNegativo += 1
            elif selector > 0:
                contadorPositivos += 1
        if contadorPositivos > contadorNegativo and contadorPositivos > cantidad_ceros:
            alert(title="titulo", message=f"Se a ingresado mas numeros positivos, una cantidad de: {contadorPositivos}")
        elif contadorNegativo > contadorPositivos and contadorNegativo > cantidad_ceros:
            alert(title="titulo", message=f"Se a ingresado mas numeros negativos, una cantidad de: {contadorNegativo}")
        else:
            alert(title="titulo", message=f"Se a ingresado mas ceros, una cantidad de: {cantidad_ceros}")

        maximo = max(self.lista_numeros)
        numeros_mayor = [Nmayor for Nmayor in self.lista_numeros if maximo == Nmayor]

        alert(title="titulo",message=f"La lista de los numeros negativos sumados es de: {numeros_negativos}\nLa suma de los numeros positivos es de: {numeros_positivos}\nLa cantidad de numeros negativos es de: {cantidad_negativos}\nLa cantidad de numeros positivos es de: {cantidad_positivos}\nLa cantidad de 0 ingresados en total es de: {cantidad_ceros}\nEl minimo de los numeros negativos es de: {num_mas_neg}\nEl maximo de los numeros positivos es de: {num_max_pos}\nEl promedio de los numeros negativos es de: {promedioNumNegativo}\nLa cantidad de numeros pares es de: {cantidadPar}, y la lista esta: {numerosPares}\nEsta es la lista de numeros mayor, puede ser uno o mas de uno en caso de que haya mas: {numeros_mayor} ")

        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
