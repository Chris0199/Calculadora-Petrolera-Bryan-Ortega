import tkinter as tk

ventana = tk.Tk()
ventana.title("Facilidades de Producción")
ventana.geometry("400x500+700+100")
ventana.minsize(width=400, height=500)
ventana.configure(bg="gray")

def convertir():

    try:
        caudal = entrada_caudal.get()
        resultado = (float(caudal)*0.029167)
        resultado1 = (float(caudal)*0.001179867)
        rotulo_resultado.config(text=resultado)
        rotulo_resultado1.config(text=resultado1)
        
    except ValueError:
        pass

def borrar() :
    rotulo_resultado.config(text=0)
    rotulo_resultado1.config(text=0)
    
    
rotulo_titulo = tk.Label(ventana, 
	text="CALCULADORA PETROLERA",
    bg="white", fg="red",
    font= "courier 20 bold",
    relief = tk.GROOVE, bd=2,
    padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

rotulo_titulo = tk.Label(ventana, 
	text="CONVERSOR CAUDAL",
    bg="white", fg="black",
    font= "courier 20 bold",
    relief = tk.GROOVE, bd=2,
    padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

cuadro1 = tk.Frame(ventana,
    bg="white")

rotulo_caudal = tk.Label(cuadro1,
    text="Caudal bbl/dia:",
    bg="white",
    font="courier 18 bold",
    width=12,
    anchor=tk.W)
rotulo_caudal.pack(side=tk.LEFT, padx=10, pady=10)

entrada_caudal = tk.Entry(cuadro1,
    bg="white", fg="black",
    font="courier 18 bold",
    relief=tk.SUNKEN,
    width=10,
    justify=tk.RIGHT,
    state="normal")
entrada_caudal.pack(side=tk.LEFT, padx=10, pady=10)

cuadro1.pack(pady=10)


cuadro2 = tk.Frame(ventana,
    bg="white")

rotulo_gpm = tk.Label(cuadro2,
    text="Caudal gpm:",
    bg="white",
    font="courier 18 bold",
    width=12,
    anchor=tk.W)
rotulo_gpm.pack(side=tk.LEFT, padx=10, pady=10)

rotulo_resultado = tk.Label(cuadro2,
    text="",
    bg="white",
    font="courier 18 bold",
    width=10,
    relief = tk.GROOVE,
    anchor=tk.E)
rotulo_resultado.pack(side=tk.LEFT, padx=10, pady=10)

cuadro2.pack(pady=10)

cuadro5 = tk.Frame(ventana,
    bg="white")

rotulo_mh = tk.Label(cuadro5,
    text="Caudal m3/h:",
    bg="white",
    font="courier 18 bold",
    width=12,
    anchor=tk.W)
rotulo_mh.pack(side=tk.LEFT, padx=10, pady=10)

rotulo_resultado1 = tk.Label(cuadro5,
    text="",
    bg="white",
    font="courier 18 bold",
    width=10,
    relief = tk.GROOVE,
    anchor=tk.E)
rotulo_resultado1.pack(side=tk.LEFT, padx=10, pady=10)

cuadro5.pack(pady=10)

cuadro3 = tk.Frame(ventana,
    bg="white")

boton_borrar = tk.Button(cuadro3,
    text="Borrar",
    bg="green",
    font="courier 18 bold",
    width=10,
    command=borrar)
boton_borrar.pack(side=tk.LEFT, padx=20, pady=20)

boton_convertir = tk.Button(cuadro3,
    text="Convertir",
    bg="blue",
    font="courier 18 bold",
    width=10,
    state="normal",
    command=convertir)
boton_convertir.pack(side=tk.LEFT, padx=20, pady=20)

cuadro3.pack(pady=10)


entrada_caudal.focus()

ventana.mainloop()
