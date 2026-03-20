import tkinter as tk

puntos = 0

def sumar_punto():
    global puntos
    puntos += 1
    puntuacion.config(text=str(puntos))

principal = tk.Tk()

principal.title("Cliker")
principal.geometry("600x400")

titulo = tk.Label(principal, text="Clica el boton para sumar puntos", font=("Arial",25))
titulo.pack(side="top", pady=20)

boton = tk.Button(principal,text="        ", command=sumar_punto)
boton.pack(padx=10,pady=50, anchor="center")

puntuacion = tk.Label(principal, text=f"{puntos}", font=("Arial", 25))
puntuacion.pack(padx=10,pady=50, anchor="center")

principal.mainloop()