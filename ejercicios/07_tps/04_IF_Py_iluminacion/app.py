import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        cantidad = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()
        lamparas_precio = 800
        subtotal = 0
        descuento_adicional = 0
        total = 0
        match (cantidad):
            case 1 | 2:
                descuento = 0
            case 3:
                match(marca):
                    case "ArgentinaLuz":
                        descuento = 0.15
                    case "FelipeLamparas":
                        descuento = 0.1
                    case _:
                        descuento = 0.05
            case 4:
                match (marca):
                    case "ArgentinaLuz" | "FelipeLamparas":
                        descuento = 0.25
                    case _:
                        descuento = 0.2
            case 5:
                match (marca):
                    case "ArgentinaLuz":
                        descuento = 0.4
                    case _:
                        descuento = 0.3
            case _:
                descuento = 0.5
            


        subtotal = (cantidad * lamparas_precio) * descuento
        total = (cantidad * lamparas_precio) - subtotal
        if total > 4000:
            descuento_adicional = total * 0.05
            
        total -= descuento_adicional
        print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}, por que supero los 4000 se le agrega un descuento adicional de {descuento_adicional}")
        pass
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    '''
        cantidad = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()
        lamparas_precio = 800
        subtotal = 0
        descuento_adicional = 0
        total = 0
        if cantidad >= 6:
            subtotal = (lamparas_precio * cantidad) *0.5
            total =  (lamparas_precio * cantidad) - subtotal
            print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}")
            if total > 4000:
                    descuento_adicional = total * 0.05
                    total = total + descuento_adicional
                    print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}, por que supero los 4000 se le agrega un descuento adicional de {descuento_adicional}")
        elif cantidad == 5:
            if marca == "ArgentinaLuz":
                subtotal = ( lamparas_precio * cantidad ) * 0.4
                total = (lamparas_precio * cantidad) - subtotal 
                print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}")
                if total > 4000:
                    descuento_adicional = total * 0.05
                    total = total + descuento_adicional
                    print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}, por que supero los 4000 se le agrega un descuento adicional de {descuento_adicional}")

            elif marca:
                subtotal = (lamparas_precio * cantidad) * 0.3
                total = (lamparas_precio * cantidad) - subtotal
                print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}")
                if total > 4000:
                    descuento_adicional = total * 0.05
                    total = total + descuento_adicional
                    print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}, por que supero los 4000 se le agrega un descuento adicional de {descuento_adicional}")
        elif cantidad == 4 :
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                subtotal = (lamparas_precio * cantidad) *0.25
                total = (lamparas_precio * cantidad) - subtotal
                print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}")
                
            elif marca :
                subtotal = (lamparas_precio * cantidad) * 0.2
                total = (lamparas_precio * cantidad) - subtotal
                print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}")
                
        elif cantidad == 3:
            if marca == "ArgentinaLuz":
                subtotal = (lamparas_precio * cantidad) *0.15
                total = (lamparas_precio * cantidad) - subtotal
                print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}")
                
            elif marca == "FelipeLamparas":
                subtotal = (lamparas_precio * cantidad) *0.1
                total = (lamparas_precio * cantidad) - subtotal
                print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}")
                
            elif marca:
                subtotal = (lamparas_precio * cantidad) * 0.05
                total = (lamparas_precio * cantidad) - subtotal
                print(f"El total es de {total} por la cantidad de {cantidad} lamparitas {marca} con un descuento de {subtotal}, por que supero los 4000 se le agrega un descuento adicional de {descuento_adicional}")
                '''