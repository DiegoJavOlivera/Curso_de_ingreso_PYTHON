import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Piedra, Papel o Tijera (v 2.0):
    Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
	El jugador seleccionará mediante uno de los botones su opción  y le informaremos si ganó, empató o perdió

Ahora debemos informar cuantas veces se ganó, perdió o empató
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_piedra = customtkinter.CTkButton(master=self, text="Piedra", command=self.btn_piedra_on_click)
        self.btn_piedra.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_papel = customtkinter.CTkButton(master=self, text="Papel", command=self.btn_papel_on_click)
        self.btn_papel.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_tijera = customtkinter.CTkButton(master=self, text="Tijera", command=self.btn_tijera_on_click)
        self.btn_tijera.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_restart = customtkinter.CTkButton(master=self, text="RESTART", command=self.btn_restart_on_click, fg_color="red")
        self.btn_restart.grid(row=5, pady=20, columnspan=2, sticky="nsew")
        
        
        
        
        self.contador_vitorias_cpu = 0 
        self.contador_vitorias_player_1 = 0 
        self.contador_empates = 0



    def deshabilitar_botones(self):
        self.btn_piedra.configure(state="disabled")
        self.btn_papel.configure(state="disabled")
        self.btn_tijera.configure(state="disabled")

    def btn_restart_on_click(self):
        self.btn_piedra.configure(state="normal")
        self.btn_papel.configure(state="normal")
        self.btn_tijera.configure(state="normal")
        self.cpu_elije()
        print(self.cpu_elije)
        print("Empates: ",self.contador_empates,"\n","Victoria CPU: ",self.contador_vitorias_cpu,"\n","Victoria Player: ",self.contador_vitorias_player_1 )

    def cpu_elije(self):
        eleccion_cpu = random.randint(1,3)
        match eleccion_cpu:
            case 1:
                
                return eleccion_cpu
            case 2:
                
                return eleccion_cpu
            case 3:
                
                return eleccion_cpu
        pass

    def btn_piedra_on_click(self):
        cpu_eleccion = self.cpu_elije()
        match cpu_eleccion:
            case 1:
                print("Cpu elige Piedra, Elegiste Piedra, Empate!, vuelve a intentarlo")
                self.contador_empates += 1
            case 2:
                print("Cpu elige Papel, Elegiste Piedra, Perdite!, Papel emvuelve Piedra")
                self.contador_vitorias_cpu += 1
            case 3:
                print("Cpu elige Tijera, Elegiste Piedra, Ganaste!, Piedra gana a tijera")
                self.contador_vitorias_player_1 += 1
        self.deshabilitar_botones()
        pass

    def btn_papel_on_click(self):
        cpu_eleccion = self.cpu_elije()
        match cpu_eleccion:
            case 1:
                print("Cpu elige Piedra, Elegiste Papel, Ganaste!, Papel emvuelve Piedra")
                self.contador_vitorias_player_1 += 1
            case 2:
                print("Cpu elige Papel, Elegiste Papel, Empate!, Vuelve a intentarlo")
                self.contador_empates += 1
            case 3:
                print("Cpu elige Tijera, Elegiste Papel, Perdiste!, Tijera corta Papel")
                self.contador_vitorias_cpu += 1
        self.deshabilitar_botones()
        pass

    def btn_tijera_on_click(self):
        cpu_eleccion = self.cpu_elije()
        match cpu_eleccion:
            case 1:
                print("Cpu elige Piedra, Elegiste Tijera, Perdiste!, Piedra gana a Tijera")
                self.contador_vitorias_cpu += 1
            case 2:
                print("Cpu elige Papel, Elegiste Tijera, Ganaste!, Tijera corta Papel")
                self.contador_vitorias_player_1 += 1
            case 3:
                print("Cpu elige Tijera, Elegiste Tijera, Empate!, Vuelve a intentarlo")
                self.contador_empates += 1
        self.deshabilitar_botones()
        pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()