import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        estacion = self.combobox_estaciones.get()
        destiny = self.combobox_destino.get()
        price_plus20 = 15000 + (15000*0.20)
        price_plus10 = 15000 + (15000*0.10)
        price_des10 = 15000 - (15000*0.10)
        price_des20 = 15000 - (15000*0.20)

        match estacion:
            case "Invierno":
                match destiny:
                    case "Bariloche":
                        alert(title="titulo",message=f"En invierno Bariloche tiene un 20% de aumento, el precio base es de 15000 y total con el aumento es {price_plus20}")
                    case "Cataratas"|"Cordoba":
                        alert(title="titulo",message=f"En invierno Cataratas y Cordoba obtiene un descuento del 10%, precio base es de 15000 y el total con el descuento es {price_des10}")
                    case "Mar del plata":
                        alert(title="titulo",message=f"En invierno Mar del plata obtiene un descuento del 20%, precio base es de 15000, en total con el descuento es de {price_des20} ")
            case "Verano":
                match destiny:
                    case "Bariloche":
                        alert(title="titulo",message=f"En verano Bariloche obtiene un descuento del %20, el precio base es de 15000 y el total con el descuento es {price_des20}")
                    case "Cataratas"|"Cordoba":
                        alert(title="titulo",message=f"En verano Cataratas y Cordoba obtiene un aumento del 10%, precio base es de 15000 y el total con el aumento es {price_plus10}")
                    case "Mar del plata":
                        alert(title="titulo",message=f"En verano Mar del plata obtiene un aumento del 20%, precio base es de 15000, en total con el aumento es de {price_plus20} ")
            case "Primavera"|"Otoño":
                match destiny:
                    case "Bariloche":
                        alert(title="titulo",message=f"En primavera u otoño Bariloche tiene un 10% de aumento, el precio base es de 15000 y el total con el aumento es {price_plus10}")
                    case "Cataratas":
                        alert(title="titulo",message=f"En primavera u otoño Cataratas obtiene un aumento del 10%, precio base es de 15000 y el total con el aumento es {price_plus10}")
                    case "Mar del plata":
                        alert(title="titulo",message=f"En primavera u otoño Mar del plata obtiene un aumento del 10%, precio base es de 15000, en total con el aumento es de {price_plus10} ")
                    case "Cordoba":
                        alert(title="titulo", message=f"En primavera u otoño Cordoba no posee descuentos u aumentos el total es de 15000")
                    
        pass
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()