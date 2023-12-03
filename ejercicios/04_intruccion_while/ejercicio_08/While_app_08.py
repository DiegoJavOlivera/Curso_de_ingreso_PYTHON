import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        sumaAcumulada = 0
        producto = 1
        while True: 
            solicitar = prompt(title="titulo",prompt="ingresar un numero, si es positivo suma, si es negativo se multiplica")
            
            if  solicitar is None:
                alert(title="titulo" , message="el usuario presiono cancelar, se muestran los resultados.")
                break            
            
            solicitar = int(solicitar)
            if  solicitar < 0:
                producto *= solicitar
                alert(title="titulo",message=f"se ingreso {solicitar} un numeor negativo, se multiplica")
            elif solicitar > 0: 
                sumaAcumulada += solicitar
                alert(title="titulo", message=f"se a ingresado un numero positivo {solicitar}, se suma")
            elif solicitar == 0:
                alert(title="titulo",message="el usuario a ingresado 0 , se cancela y se muestran los resultados")
                break
            
        self.txt_suma_acumulada.insert(0,sumaAcumulada)
        self.txt_producto.insert(0,producto)


        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
