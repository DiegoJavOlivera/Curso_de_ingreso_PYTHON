import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        try:
            produc1 = int(self.txt_importe_1.get())
            produc2 = int(self.txt_importe_2.get())
            produc3 = int(self.txt_importe_3.get())
            suma = 0
            suma += produc1 + produc2 + produc3 
            alert(title="titulo",message=f"La suma de todos los productos ingresados es {suma}")
        except:
            alert(title="titulo",message="El usuario ingreso una latra, intente nuevamente, intentar denuevo y ingresar un numero")
            pass

    def btn_promedio_on_click(self):
        try:
            produc1_promedio = int(self.txt_importe_1.get())
            produc2_promedio = int(self.txt_importe_2.get())
            produc3_promedio = int(self.txt_importe_3.get())
            suma = 0
            cantidad_produc = 3
            suma += produc1_promedio + produc2_promedio + produc3_promedio
            suma /= cantidad_produc
            alert(title="titulo",message=f"el promedio de los 3 productos es {int(suma)}")
        except:
            alert(title="titulo",message="El usuario ingreso una letra, intentar denuevo y ingresar un numero")
        pass

    def btn_total_iva_on_click(self):
        try:
            produc1_iva = int(self.txt_importe_1.get())
            produc2_iva = int(self.txt_importe_2.get())
            produc3_iva = int(self.txt_importe_3.get())
            suma = 0
            suma += produc1_iva + produc2_iva + produc3_iva
            total = suma
            suma *= 0.21
            totalIva = suma
            total += suma
            alert(title="titulo",message=f"El total de los 3 productos del 21% es de {totalIva}, el total del precio final es de {total}")
        except:
            alert(title="titulo",message="El usuario ingreso una letra, intentar denuevo y ingresar un numero")
        pass      
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()