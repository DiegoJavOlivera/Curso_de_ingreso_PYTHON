import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        lista_numeros_negativos = []
        lista_numeros_positivos = []
        lista_numero_cero = []
        while True:
            solicitar_numero = prompt(title="solicitar numero",prompt="Ingresa un numero ")
            if solicitar_numero is None:
                alert(title="Titulo cancelar",message="El usuario a presionado Cancelar")
                break
            solicitar_numero = int(solicitar_numero)
            if solicitar_numero > 0:
                lista_numeros_positivos.append(solicitar_numero)
            elif solicitar_numero < 0:
                lista_numeros_negativos.append(solicitar_numero)
            elif solicitar_numero == 0:
                lista_numero_cero.append(solicitar_numero)

        suma_positivos = sum(lista_numeros_positivos)
        suma_negativos = sum(lista_numeros_negativos)
        cantidad_positivos = len(lista_numeros_positivos)
        cantidad_negativos = len(lista_numeros_negativos)
        diferencia_cantidad = cantidad_positivos - cantidad_negativos
        cantidad_ceros = len(lista_numero_cero)


        alert(title="titulo con resultados",message=f"La suma acumulada de negativos es: {suma_positivos} \nLa suma acumulada de numeros negativos es:  {suma_negativos}\nCantidad de numeros positivos: {cantidad_positivos}\nCantidad de numeros negativos: {cantidad_negativos}\nCantidad de ceros: {cantidad_ceros}\nDiferencia entre la cantidad de positivos y negativos: {diferencia_cantidad} ")


        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
