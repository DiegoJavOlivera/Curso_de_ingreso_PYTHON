import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        solicitar = prompt(title="titulo",prompt="Ingresa un numero")
        solicitar = int(solicitar)
        divisor = 0
        for i in range(1, solicitar + 1):
            if solicitar % i == 0:
                divisor += 1
    
        if divisor == 2:
            print(f"El numero {solicitar} es un numero primo y tiene 2 divisores 1 y a si mismo")
        else:
            print("no es numero primo")
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()