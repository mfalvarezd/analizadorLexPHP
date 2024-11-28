import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as st
import main as sn
import AnalizadorLexPHP as lx

from datetime import datetime 

today = datetime.now()

valorLexico= lx.lexer
valorsintatico= sn.parser
analizadorLexico=lx.obtener_validador_lexico()
analizadorSintactico= sn.obtener_analizador_sintactico()

logs_file = open ('logs.txt','w')


## Root GUI
root = tk.Tk()
root.title("Analizador PHP")
root.resizable(False, False)
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

ancho_ventana = 1100 
alto_ventana = 800 

## Etiqueta Principal
etiqueta = tk.Label(root, text="ANALIZADOR DE CÓDIGO PHP" , fg="#FFFFFF", bg='#FADF9D',  font=("Arial", 25) )
etiqueta.grid(row = 0, column = 0, padx = 15, columnspan=2)

##Etiqueta Ingreso
mensaje_in = tk.Label(root, text="Ingrese su código aquí:" , bg='#FADF9D',  font=("Arial", 12))
mensaje_in.grid(row = 1, column = 0, padx = 2)

## Caja de ingreso
cajatexto = tk.scrolledtext.ScrolledText(root, width= 80, height = 12, wrap=WORD)
cajatexto.grid(row=2, column=0, padx=20, pady=20, rowspan=5)


#Analisis lexico
def lexico():
    codigo = cajatexto.get("1.0", END)
    logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ "\n")
    logs_file.write("Entrada:"+"\n" +codigo+"\n")
    resultadoLex.configure(state='normal')
    resultadoLex.delete("1.0", END)
   
    lista_tokens = [] 
    analizadorLexico.input(codigo)
    lx.getTokens(analizadorLexico, lista_tokens)   
    logs_file.write("Salida:"+"\n")


    for i in range(0,len(lista_tokens)):
        logs_file.write(str(lista_tokens[i])+"\n")
        resultadoLex.insert( float(i+1), str(lista_tokens[i])+"\n")
    
    resultadoLex.configure(state='disabled') 

#Boton analisis lexico
botonLex = tk.Button(root, text="Analizar Léxico", width = 15, height=2, bg='#FA8726', command=lexico)
botonLex.grid(row = 3, column = 1, padx = 15)

## Caja de salida lexico
resultadoLex = tk.scrolledtext.ScrolledText(root, width= 80, height = 12, wrap=WORD)
resultadoLex.grid(row = 12, column=0, padx = 20 ,pady = 20, rowspan=5)
resultadoLex.configure(state='disabled')   


def sintatico():
    #obtenemos el codigo
    codigo = cajatexto.get("1.0", END)

    logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+ "\n")
    logs_file.write("Entrada:"+"\n" +codigo+"\n")
    resultadoLex.configure(state='normal')
    resultadoLex.delete("1.0", END)

    logs_file.write("Salida:"+"\n")
    
    analisis = str(analizadorSintactico.parse(codigo))   
    
    if len(sn.errores_sintaxis) > 0:
        
        for i in range(len(sn.errores_sintaxis)):
            logs_file.write(str(sn.errores_sintaxis[i])+"\n")
            resultadoLex.insert( float(i+1), str(sn.errores_sintaxis[i])+"\n")
        sn.errores_sintaxis.clear() 
    else:
        # Insertamos el resultado
       resultadoLex.insert("1.0", "Ingreso Válido")

    resultadoLex.configure(state='disabled')   
        
botonSin = tk.Button(root, text="Analizar Sintáxis", width = 15, height=2, bg='#FA8726',command=sintatico)
botonSin.grid(row = 4, column = 1, padx = 15)


def limpiar():
    cajatexto.delete("1.0", END)
    resultadoLex.configure(state='normal')
    resultadoLex.delete("1.0", END)

b_limpiar = tk.Button(root, text="Limpiar", width = 10, height=2, bg='#FA8726',command=limpiar)
b_limpiar.grid(row = 14, column = 1, padx = 15, columnspan=1)

root.configure(bg='#FADF9D')
root.mainloop()
