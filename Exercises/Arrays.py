#/////////////////////////////////////////////////////////////////// 
#/////////////////          Jesus Gaspar          ////////////////// 
#/////////////////////////////////////////////////////////////////// 

#Ejercicio 1: Actualización de Miembros de una Banda   

i=1 
miembros = ["Alice","John","Luz"] 
miembros.append("Davis") 
miembros.append("Scot") 

print("Lista: ",miembros) 

print("\nIngrese dos integrantes más: ") 

for i in range(2): 
    integrante = input("Cuál es el nombre del integrante?: ") 
    miembros.append(integrante) 
    i+=1 
    
print("Lista actual: ",miembros) 

del miembros[6] 

miembros.insert(2,"Frank") 

print("\nLista final: ",miembros) 


#Ejercicio 2: Gestión de Inventario de Tienda   

print("\n\n")

inventario = [] 

inventario.append("Leche") 

inventario.append("Huevos") 

inventario.append("Arina") 

inventario.append("Arroz")

inventario.append("Papas") 

print("El inventario es: ",inventario) 

for i in range(0,3): 
    producto = input("Agregue un artículo: ") 
    inventario.append(producto) 
    i+=1 

print("El inventario actual es: ",inventario) 

del inventario[2:4] 

inventario.insert(0,"galletas")

print("\nEl inventario actualizado es: ",inventario) 



#Ejercicio 3 Planificación de Tareas   

print("\n\n") 

tareas = [] 

tareas.append("Desayunar"),tareas.append("Estudiar Python"),tareas.append("GYM")

xd=3 

for i in range(2): 
    xd -= 1 
    nuebo=input(f"Inserte {xd} actividades mas: ")
    tareas.append(nuebo) 

print(tareas) 

del tareas[0] 

print(tareas) 

tareas.append("Preparar cena") 

print(tareas) 


#Ejercicio 4 Ordenamiento de Números enteros   

my_list = [5,3,8,1,2] 

swapped = True 

print("\n\nDesordenada:") 


print(my_list) 

while swapped: 
    swapped = False 
    for i in range(len(my_list) - 1): 
        if my_list[i] > my_list[i + 1]: 
            swapped = True 
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 

print("\nOrdenada:") 

print(my_list) 


#Ejercicio 5: Ordenamiento de Palabras por Longitud   


print("\n\n") 

Mi_lista = ["Python", "es", "genial", "para", "aprender"] 

def ordenación_chida(Mi_lista): 
    
    n = len(Mi_lista) 
    
    for y in range(n): 
        for x in range(0, n-y-1): 
            if len(Mi_lista[x]) > len(Mi_lista[x+1]):  
                Mi_lista[x], Mi_lista[x+1] = Mi_lista[x+1], Mi_lista[x] 

ordenación_chida(Mi_lista) 

print("La lista ordenada por longitud de palabra sería:",Mi_lista) 


#Ejercicio 6: Ordenamiento de Precios de Productos   

print("\n\n") 

precios = [19.99, 9.99, 14.99, 29.99, 4.99] 

def descendente(lista): 

    n = len(lista) 

    for y in range(n): 
        for x in range(0, n-y-1): 
            if lista[x] < lista[x+1]: 
                lista[x], lista[x+1] = lista[x+1], lista[x] 
            
descendente(precios)      
print("Los precios ordenados desendentes serían:",precios) 

# Ejercicio 7: Manipulación de Rebanadas en una Lista de Números   


print("\n\n")

números = [10, 20, 30, 40, 50, 60] 

print("Lista números:", números) 

números = números[3:] 

pares = números[:3] 

print("Lista números:", números) 

print("Lista pares:", pares) 



# Ejercicio 8: Rebanadas para Manipular una Lista de Palabras   

print("\n\n") 

palabras = ["Manzana", "Banana", "Cereza", "Durazno", "Uva", "Pera"] 

print("Lista palabras:", palabras) 

frutas_cortas = palabras[:3] 

palabras = palabras[:-2] 

palabras, frutas_cortas 

print("Lista palabras:", palabras) 


print("Lista frutas_cortas:", frutas_cortas) 


#Ejercicio 9: Verificación de Elementos en una Lista de Compra   

print("\n\n") 

Lista_compras= {"pan", "leche", "huevos", "fruta", "carne"} 

print("La lista es: ",Lista_compras)

verificar= input("Que vas a verificar en la lista de compras? ")

if verificar in Lista_compras: 
    print(f"El elemento '{verificar}' esta en la lista de compras") 

else: 
    print(f"El elemento '{verificar}' no esta en la lista de compras") 


#Ejercicio 10: Filtrado de Elementos en una Lista de Números   

print("\n\n") 

lista= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 

print("La lista es: ", lista) 

lista_impar= [] 

for numero in lista:
    if numero not in {2, 4, 6, 8, 10}: 
        lista_impar.append(numero) 

print("Numeros Impares", lista_impar)