#/////////////////////////////////////////////////////////////////// 
#/////////////////          Jesus Gaspar          ////////////////// 
#/////////////////////////////////////////////////////////////////// 

#1.1 Año bisiesto 

def leap(): 

    global b 

    b=False  

    if año%4==0 or año%400==0: 

        b=True 

        return (print("El",año,"es bisiesto")) 

    else: 

        return (print("El",año,"no es bisiesto")) 

 

#1.2 Días 

 

def dias(): 

     

    if mes==4 or mes==6 or mes==9 or mes==11: 

        return(print("El mes número",mes,"tiene 30 días\n")) 

    elif mes==2 and (año%4==0 or año%400==0): 

        return(print("El mes número",mes,"tiene 29 días\n")) 

    elif mes==2: 

        return(print("El mes número",mes,"tiene 28 días\n")) 

    else: 

        return(print("El mes",mes,"tiene 31 días\n")) 

 

def verif(): 

    if año<1582: 

        return (print("Año no válido por calendario gregoriano NONE")) 

    if mes > 12 or mes < 1: 

        return (print("NONE")) 

    else: 

     leap() 

     dias() 

     nd() 

 

#2 Dia del año con fecha 

 

def nd(): 

    n=int(input("Ingrese un día de su mes elegido: ")) 

    if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (n < 1 or n > 30): 

            return (print("NONE")) 

    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (n < 1 or n > 31): 

            return (print("NONE")) 

    if (año%4==0 or año%400==0) and (mes == 2) and (n > 29 or n < 1): 

            return (print("NONE")) 

    elif (b is False) and (mes == 2) and (n > 28 or n < 1): 

            return (print("NONE")) 

    if año%4==0 or año%400==0: 

        list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

        dia=sum(list[0:mes-1])+n 

        return (print("Esta en el día",dia,"del año",año)) 

     

    else: 

        list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

        dia=sum(list[0:mes-1])+n 

        return (print("Estas en el día",dia,"del año",año)) 

 

año=int(input("Ingrese un año de su elección: ")) 

 

if año>=1582: 

    mes=int(input("Ingrse número del mes que quiera: ")) 

    print("\n") 

 

verif() 

 

#////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

#////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

 

print("\n") 

 

#3 Ejercicio 3: Conversión de Unidades de Consumo de Combustible 

 

def litros(): 

    l=float(input("Ingrese la cantidad de litros de gasolina: ")) 

    cons=l/100 

    gal=l/3.785411784 

    mi=100*1.61 

    mpg=gal/mi 

    print("Su consumo de L/KM por 100Km es: ",round(cons,2)) 

    return (print("Su consumo convertido es: ",round(mpg,2))) 

 

def galones(): 

    gal=float(input("Ingrese la cantidad de galones de gasolina: ")) 

    cons=gal/100 

    l=3.785411784*gal 

    km=100*0.621371 

    KL=l/km 

    print("\nSu consumo en mpg por 100mi es: ",round(cons,2)) 

    return (print("\nSu consumo convertido es: ",round(KL,2))) 

 

desision=input(("Que desea convertir? (KM o MI): ")) 

 

if desision == "KM": 

        litros() 

elif desision == "MI": 

        galones() 

else: 

    print("Valor no válido") 

 