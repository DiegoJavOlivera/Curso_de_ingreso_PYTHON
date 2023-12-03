'''
alert = showinfo manda una ventana emergente utilizando tkinter se importa como "showinfo"{
 se le puede ingresar titulo con "title=str" y un mensaje con "message=str"}

question = askyesno similar al alert() pero para preguntar al usuario una confirmacion o rechazo, resultado puede ser true o false, utilizando tkinter se importa como "askyesno" y va dentro de una variable por ejemplo "result = question(title="question", message="desea continuar?") ".  

prompt = asktring muesta un cuadro con dialogo donde podemos solicitar valor al usuario
se importa como askstring de tkinter y funciona como "result = prompt(title="prompt", prompt="ingrese un valor" )"

obtener datos get() = con get podemos obtener el valor ingresado de una caja de texto usando "valor= self.txt_nombre.get()"   

delete() = podemos borrar el contenido usando self.txt_resultado.delete(0,100) si o si 0 hasta donde querramos borrar

insert() = podemos insertar valores nuevos con self.txt_resultado.insert(0, valor_resultado)

int() = es para pasar de string a valor entero

% = el operador resto muestra el resto de una division 

random = te permite generar numeros aleatorios importando la biblioteca "import random" tenes varios ejemplos "random.random()" para 0 y 1 , "random.randint(1,100)" para numeros enteros, "random.uniform(0,1.0)" para dentro de ese rango. "random.choice(mi_lista)" dentro del parentesis representa un array con una lista de numeros 
. "random.shuffle(mi_lista)" para mezclar aleatoriamente una lista 

lower() = convierte el texto a minuscula 

is none= en python se utiliza para representar la ausencia de un valor o para indicar que no se ha seleccionado ninguna opcion


True = dentro de un while true funciona para que comience el ciclo y que no se detenga, por que mientras sea true el ciclo continuara break es para cancelar el ciclo

.isnumeric() = verifica si la cadena contiene solo numeros, si es asi retorna true sino false por ejemplo "123ab" retorna false por que contiene 2 string

isdigit()= verifica si el contenido es un digito 

append() = funciona para agregar elementos al final de una lista array 

max()= retorna el numero maximo de una listase, se debe pasar una lista como argumento

min()= retorna el minimo de una lista

sum() = se usa para sumar todos los elementos de una liusta sin necesidad de usar un bucle for

len() = devuelve la cantidad de  elementos (longitud) que contiene la lista
dentro de los parentesis va la lista 

for in range() se usa para iterar sobre una secuencia de numeros especificados dentro de range() tambien si quieres recibir un numero en especifico de algun lado puedes usarlo dentro del for Con un bucle for se puede mostrar una lista para recorrerla

El metodo join() se utuliza para unir los elementos de una lista en una cadena, se le puede colocar algo adelante como una coma para poder separarlos y cargadado en una variable 

en match usar el guion bajo _ en case es para que seleccione cualquier otro

math.srqt() sirve para encontrar la raiz cuadrada de la variable que va a estar dentro de los parentesis 

set() se utiliza en tkinter para establecer el valor seleccionado en un widget de tipo combobox

.index() te da el indice de la lista

.count() se utiliza para contar cuantas veces un elemento especifico aparece ene esa secuencia, toma como argumento lo que deseas contar y devuelve el numero de veces que ese elemento esta presente en la secuencia 

 key=candidatos.get con la función max() para encontrar la clave (en este caso, el nombre del candidato) que tenga el valor máximo asociado en el diccionario candidatos. La función candidatos.get se usa como función de clave, lo que significa que para cada elemento (en este caso, cada nombre de candidato) max() llamará a candidatos.get(nombre) para obtener su valor correspondiente en el diccionario candidatos y luego encontrará el nombre que tenga el valor máximo asociado a él.

'''


