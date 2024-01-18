# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "Diego" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4) = 7

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9. 9-7 = 2

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=6, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        self.lista_nombre = ["Pepe", "Paola", "Dardo", "Fatiga", "Maria"]
        self.lista_monto = [20000,30000,40000,50000,60000]
        self.lista_tipo_instrumento = ["CEDEAR","BONOS","MEP","CEDEAR","CEDEAR"]
        self.lista_cantidad_instrumento = [20, 35, 199, 100, 80]
    def btn_cargar_datos_on_click(self):
        contador = 0
        while contador < 10:
            while True:
                ingresar_nombre = prompt(title="titulo",prompt="Ingrese su nombre")
                if any(texto.isnumeric() for texto in ingresar_nombre):
                    print("El usuario a ingresado numero en su nombre, intente nuevamente")
                elif ingresar_nombre.isalpha():
                    self.lista_nombre.append(ingresar_nombre)
                    print("El usuario a ingresado su nombre correctamente")
                    break
                else:
                    print("Intentar nuevamente")
            while True:
                ingresar_monto = prompt(title="titulo", prompt="Ingrese un monto no menor a $10000")
                if any(numero.isalpha() for numero in ingresar_monto):
                    print("Ingreso un texto en el monto, vuelva a intentar")
                elif int(ingresar_monto) < 10000:
                    print("a ingresado un monto menor a 10000, intentarlo denuevo")
                elif int(ingresar_monto) > 10000:
                    self.lista_monto.append(ingresar_monto)
                    print("Se a ingresado el monto correctamente")
                    break
                else:
                    print("Intentar nuevamente")
            while True:
                instrumento_tipo = prompt(title="titulo", prompt="Ingresar el tipo de instrumento: CEDEAR , BONOS, MEP").upper()
                if any(texto.isnumeric() for texto in instrumento_tipo):
                    print("El usuario ingreso un numero en texto, intentelo nuevamente")
                elif instrumento_tipo == "CEDEAR" or instrumento_tipo == "BONOS" or instrumento_tipo == "MEP":
                    self.lista_tipo_instrumento.append(instrumento_tipo)
                    print("El usuario ingreso el tipo de instrumento")
                    break
                else:
                    print("Intentar nuevamente")
            while True:
                instrumento_cantidad = prompt(title="titulo", prompt="Ingrese la cantidad de instrumentos")
                if any(numero.isalpha() for numero in instrumento_cantidad):
                    print("El usuario a ingresado un texto, Vuelva a intentarlo")
                elif int(instrumento_cantidad) < 0:
                    print("No se puede ingresar numeros negaticvos, Intentelo denuevo")
                elif int(instrumento_cantidad) > 0:
                    print("El usuario a ingresado la cantidad de instrumentos")
                    self.lista_cantidad_instrumento.append(instrumento_cantidad) 
                    break
                else:
                    print("Intentar nuevamente")
            contador += 1

        pass


    def btn_mostrar_informe_1(self):
        lista_nombre = []
        for indice, valor in enumerate(self.lista_nombre):
            lista_nombre.append((indice,valor))
        print("Lista de posicion y nombre: ",lista_nombre)

        lista_monto = []
        for indice, valor in enumerate(self.lista_monto):
            lista_monto.append((indice,valor))
        print("Lista de posicion y monto: ",lista_monto)
        
        lista_tipo_instrumento = []
        for indice,valor in enumerate(self.lista_tipo_instrumento):
            lista_tipo_instrumento.append((indice,valor))
        print("Lista de posicion y tipo de instrumento: ",lista_tipo_instrumento)

        lista_cantidad_instrumento = []
        for indice, valor in enumerate(self.lista_cantidad_instrumento):
            lista_cantidad_instrumento.append((indice,valor))
        print("Lista de posicion y cantidad de instrumento: ",lista_cantidad_instrumento)      
        pass
        


    def btn_mostrar_informe_2(self):
        ingresar_ultimo_dni = prompt(title="titulo",prompt="Ingrese su ultimo numero de DNI")
        ingresar_ultimo_dni = int(ingresar_ultimo_dni)
        return ingresar_ultimo_dni
        pass
        


    def btn_mostrar_informe_3(self):
        ingresar_ultimo_dni = prompt(title="titulo", prompt="Ingrese su ultimo numero de DNI")
        ingresar_ultimo_dni = int(ingresar_ultimo_dni)
        if ingresar_ultimo_dni == 0:
            return 9
        else:
            ingresar_ultimo_dni = 9 - ingresar_ultimo_dni 
            return ingresar_ultimo_dni
        pass      
    def informar_dosOuno(self):
        resultado_informe3 = self.btn_mostrar_informe_3()
        if resultado_informe3:
            return resultado_informe3
        else:
            return self.btn_mostrar_informe_2()

    def btn_mostrar_todos_on_click(self):
        dni_ultimo = self.informar_dosOuno()
        match dni_ultimo:
            case 0: 
                tipo_instrumento_menos_operado = min(self.lista_tipo_instrumento, key=self.lista_tipo_instrumento.count)
                print(f"El instrumento que menos se opero es {tipo_instrumento_menos_operado}")
            case 1:
                tipo_instrumento_mas_operado = max(self.lista_tipo_instrumento, key= self.lista_tipo_instrumento.count)
                print(f"El instrumento mas operador es: {tipo_instrumento_mas_operado}")
            case 2:
                lista_Cant_Instru_tipo = list(zip(self.lista_tipo_instrumento,[int(x) for x in self.lista_cantidad_instrumento]))
                cantidad_compraron_50_200Mep = sum(1 for tipo, cantida in lista_Cant_Instru_tipo if (tipo == "MEP") and cantida > 50 and cantida < 200)
                print(f"La cantidad de usuarios que compraron entre 50 y 200 MEP es: {cantidad_compraron_50_200Mep}")
            case 3:
                cant_no_cedear = sum(1 for tipo in self.lista_tipo_instrumento if tipo != "CEDEAR")
                print(f"La cantidad de usuarios que no compraron CEDEAR son : {cant_no_cedear}")
            case 4:
                list_monto_bonos = list(zip(self.lista_monto,self.lista_tipo_instrumento, self.lista_nombre))
                for monto , tipo, nombre in list_monto_bonos:
                    if tipo == "CEDEAR" or tipo == "BONOS":
                        nombre_primer = nombre
                        cantidad_monto = monto
                        tipo_instrumento = tipo
                        break
                print(f"El nombre y cantidad invertida del primer usuario que compro BONOS o CEDEAR es: {nombre_primer}, {cantidad_monto}, {tipo_instrumento}")
            case 5:
                list_nomb_posici_tipo = list(zip(self.lista_nombre,self.lista_cantidad_instrumento,self.lista_tipo_instrumento))
                min_cantidad_bonos = float('inf')
                for i, (nombre, cantidad, tipo) in enumerate(list_nomb_posici_tipo):
                    if (tipo == "BONOS")and cantidad < min_cantidad_bonos:
                        nombre_menos_bonos = nombre
                        indice = i
                print(f"El nombre y la posicion de la persona que menos BONOS compro es: {nombre_menos_bonos} posicion: {indice}")
            case 6: 
                list_nomb_menos_dinero = list(zip(self.lista_nombre, self.lista_monto))
                monto_inf = float('inf')
                for i, (nombre, monto_dinero) in enumerate(list_nomb_menos_dinero):
                    if monto_dinero < monto_inf:
                        nombre_menor_dinero = nombre
                        menor_dinero = monto
                        posicion_menos_dinero = i
                print(f"El nombre y la posicion de la persona que invirtio menos dinero es: {nombre_menor_dinero} Posicion: {posicion_menos_dinero}, Cantidad de dinero: {menor_dinero}")
            case 7:
                list_nomb_mas_instr = list(zip(self.lista_nombre,self.lista_cantidad_instrumento))
                monto_inf_inst = 0
                for i,(nombre, instrumento_canti) in enumerate(list_nomb_mas_instr):
                    if instrumento_canti > monto_inf_inst:
                        monto_inf_inst = instrumento_canti
                        posicion_mas_ins = i
                        nombre_mas_ins = nombre
                print(f"El nombre y la posicion de la persona que mas cantidad de instrumentos compro es: {nombre_mas_ins} , Posicion: {posicion_mas_ins}")
            case 8:
                monto_cedear = 0
                contador = 0
                list_monto_cedear = list(zip(self.lista_monto,self.lista_tipo_instrumento))
                for monto, tipo in list_monto_cedear:
                    if tipo == "CEDEAR":
                        monto_cedear += monto
                        contador += 1
                promedio_cedear = monto_cedear / contador
                print(f"El promedio de dinero ingresado en CEDEAR es de: {promedio_cedear}, cantidad total de dinero ingresado en CEDEAR: {monto_cedear}") 
            case 9:
                monto_mep = 0
                contador_mep = 0
                list_monto_mep = list(zip(self.lista_monto, self.lista_tipo_instrumento))
                for monto_for_mep , instrumento in list_monto_mep:
                    if instrumento == "MEP":
                        monto_mep += monto_for_mep
                        contador_mep += 1
                promedio_monto_mep = monto_mep / contador_mep
                print(f"El promedio de la cantidad de instrumentos MEP vendios es: {promedio_monto_mep}, cantidad total vendida: {monto_mep}")
        pass

        

if __name__ == "__main__":
    app = App()
    app.mainloop()
