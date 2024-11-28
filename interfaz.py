import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as st
import os
import main as smt
import AnalizadorLexPHP as lx
from datetime import datetime

# Configuración inicial
today = datetime.now()
valorLexico = lx.lexer
valorsintatico = smt.parser
analizadorLexico = lx.getAnalizadorLexico()
analizadorSintactico = smt.getAnalizadorSintactico()
logs_file = open('logs\logs.txt', 'w')

# Carpetas de trabajo
current_directory = os.path.dirname(os.path.abspath(__file__))
algoritmos_directory = os.path.join(current_directory, "algoritmos")
os.makedirs(algoritmos_directory, exist_ok=True)

# Función para listar archivos en la carpeta algoritmos
def listar_archivos():
    lista_archivos.delete(0, END)
    archivos = [f for f in os.listdir(algoritmos_directory) if f.endswith('.php')]
    for archivo in archivos:
        lista_archivos.insert(END, archivo)

# Función para mostrar contenido del archivo seleccionado
def mostrar_contenido(event):
    seleccion = lista_archivos.curselection()
    if seleccion:
        archivo = lista_archivos.get(seleccion[0])
        archivo_path = os.path.join(algoritmos_directory, archivo)
        try:
            with open(archivo_path, 'r') as f:
                contenido = f.read()
                cajatexto.delete(1.0, END)
                cajatexto.insert(END, contenido)
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudo cargar el archivo.\n{e}")

def update_line_numbers(event=None):
    line_numbers = ""
    total_lines = int(cajatexto.index('end-1c').split('.')[0])  # Obtiene el número total de líneas
    for line in range(1, total_lines + 1):
        line_numbers += f"{line}\n"
    text_line_numbers.config(state="normal")
    text_line_numbers.delete(1.0, "end")
    text_line_numbers.insert(1.0, line_numbers)
    text_line_numbers.config(state="disabled")

# Función para análisis léxico
def lexico():
    codigo = cajatexto.get("1.0", END)
    logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n")
    logs_file.write("Entrada:" + "\n" + codigo + "\n")
    resultadoLex.configure(state='normal')
    resultadoLex.delete("1.0", END)

    lista_tokens = []
    analizadorLexico.input(codigo)
    lx.getListaTokens(analizadorLexico, lista_tokens)
    logs_file.write("Salida:" + "\n")

    for i, token in enumerate(lista_tokens):
        logs_file.write(str(token) + "\n")
        resultadoLex.insert(float(i + 1), str(token) + "\n")

    resultadoLex.configure(state='disabled')

# Función para análisis sintáctico
def sintatico():
    codigo = cajatexto.get("1.0", END)
    logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n")
    logs_file.write("Entrada:" + "\n" + codigo + "\n")
    resultadoLex.configure(state='normal')
    resultadoLex.delete("1.0", END)

    logs_file.write("Salida:" + "\n")
    analisis = str(analizadorSintactico.parse(codigo))

    if smt.errores_sintacticos:
        for i, error in enumerate(smt.errores_sintacticos):
            logs_file.write(str(error) + "\n")
            resultadoLex.insert(float(i + 1), str(error) + "\n")
        smt.errores_sintacticos.clear()
    else:
        resultadoLex.insert("1.0", "Ingreso Válido")

    resultadoLex.configure(state='disabled')

# Función para limpiar contenido
def limpiar():
    cajatexto.delete("1.0", END)
    resultadoLex.configure(state='normal')
    resultadoLex.delete("1.0", END)

# GUI Principal
root = tk.Tk()
root.title("Analizador PHP")
root.resizable(True, True)
root.geometry("1000x550")
root.configure(bg='#3a7aba')

# Canvas y scrollbar
canvas = Canvas(root, bg="#3a7aba")
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#3a7aba")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Marco izquierdo: lista de archivos
frame_izquierdo = Frame(scrollable_frame, bg="#3a7aba", width=250)
frame_izquierdo.grid(row=0, column=0, rowspan=20, sticky="ns", padx=10, pady=10)

Label(frame_izquierdo, text="Algoritmos", bg="#3a7aba", fg="#FFFFFF",font=("Arial", 12, "bold")).pack(pady=5)

# Lista de archivos
lista_archivos = Listbox(frame_izquierdo, bg="white", fg="black", width=30, height=20, font=("Arial", 10))
lista_archivos.pack(fill=BOTH, expand=True, pady=5)
lista_archivos.bind("<<ListboxSelect>>", mostrar_contenido)

boton_actualizar = Button(frame_izquierdo, text="Actualizar Lista", bg="#FA8726", command=listar_archivos)
boton_actualizar.pack(fill=X, pady=5)

# Marco principal
frame_principal = Frame(scrollable_frame, bg="#3a7aba")
frame_principal.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

Label(frame_principal, text="ANALIZADOR PHP", bg="#3a7aba", fg="#FFFFFF", font=("Arial", 25)).grid(row=0, column=0, columnspan=2, pady=10)

Label(frame_principal, text="Ingrese su código aquí:", bg="#3a7aba",fg="#FFFFFF", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)

# Caja de texto de entrada con números de línea
frame_text = Frame(frame_principal)
frame_text.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

text_line_numbers = Text(frame_text, width=4, padx=4, pady=4, state="disabled", wrap="none", bg="#f0f0f0", fg="#333")
text_line_numbers.pack(side="left", fill="y")

cajatexto = st.ScrolledText(frame_text, width=80, height=15, wrap=WORD)
cajatexto.pack(side="right", fill="both", expand=True)

cajatexto.bind("<KeyRelease>", update_line_numbers)
cajatexto.bind("<MouseWheel>", update_line_numbers)

# Botones y resultados
botonLex = Button(frame_principal, text="Analizar Léxico", width=15, height=2, bg='#FA8726', command=lexico)
botonLex.grid(row=3, column=0, pady=5, sticky="e", padx=10)

botonSin = Button(frame_principal, text="Analizar Sintáxis", width=15, height=2, bg='#FA8726', command=sintatico)
botonSin.grid(row=3, column=1, pady=5, sticky="w", padx=10)

Label(frame_principal, text="Resultados del análisis:", bg="#3a7aba",fg="#FFFFFF", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5)

resultadoLex = st.ScrolledText(frame_principal, width=80, height=15, wrap=WORD)
resultadoLex.grid(row=5, column=0, columnspan=2, pady=10)
resultadoLex.configure(state='disabled')

b_limpiar = Button(frame_principal, text="Limpiar", width=10, height=2, bg='#FA8726', command=limpiar)
b_limpiar.grid(row=6, column=0, columnspan=2, pady=5)

# Inicializar lista de archivos y números de línea
listar_archivos()
update_line_numbers()

# Iniciar GUI
root.mainloop()
