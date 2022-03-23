"""
Daniel Felipe Acevedo Moreno - 201910941
Juan Pablo Martínez Pineda - 202012623
Laura María Restrepo Palomino - 202013289
Sebastián Alberto Umaña Peinado - 202013778 
"""
#Entrada
import sys

#Definición de pila
def pancakes():
    cantidad = int(sys.stdin.readline())
    for each_stack in range(cantidad):  
        flips = ""
        stack = sys.stdin.readline()
        stack = stack.split(" ")
        n = len(stack)
        for i in range(n):
            stack[i] = int(stack[i])
       
        #Verificación de orden
        j = 0
        orden = True
        while orden == True and j<n-1:
            if stack[j+1] == stack[j]-1:
                orden = True
            else:
                orden = False
            j += 1
        if orden == True:
            flips += "ORDENADO"
        
        #Flips de ordenamiento
        else:
            centinela = False
            mayor = n
            while centinela == False:
                k = 0
                orden = True
                while orden == True and k<n-1:
                    if stack[k+1] == stack[k]+1:
                        orden = True
                    else:
                        orden = False
                    k += 1
                if orden == True:
                    centinela = True
                else:
                    i_mayor = stack[:mayor].index(mayor)
                    copy_stack = stack.copy()
                    if i_mayor == 0:
                        flips += str(n-mayor) + " "
                        for l in range(mayor):
                            stack[l] = copy_stack[mayor-1-l]
                        mayor -= 1
               
                    else:
                        if i_mayor == mayor-1:
                            mayor -= 1
                        else:
                            flips += str(n-1-i_mayor) + " "  
                            for m in range(i_mayor+1):
                                stack[m] = copy_stack[i_mayor-m]
    
            copy_stack_2 = stack.copy()
            for o in range(n):
                stack[o] = copy_stack_2[n-1-o]
            flips += "0"
        
        #Salida
        print(flips)

pancakes()