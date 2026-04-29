import customtkinter as kc
import random as rd

Root = kc.CTk()
kc.set_appearance_mode("dark")

Root.after(0, lambda: Root.state("zoomed"))
Root.grid_columnconfigure(0, weight=1)
Root.grid_rowconfigure(0, weight=1)

def Tirada():
    Numero_Dado = rd.randint(1,6)
    Dado.configure(text=str(Numero_Dado))
    
Caja = kc.CTkFrame(
    Root, 
    width=500, 
    height=500, 
    corner_radius=30, 
    border_width=2, 
    border_color="#404040"
)
Caja.grid(row=0, column=0)
Caja.grid_propagate(False)
Caja.grid_columnconfigure(0, weight=1)
Caja.grid_rowconfigure((0, 1), weight=1)

Dado = kc.CTkLabel(
    Caja, 
    text="¿?", 
    font=("Comic Sans MS", 120, "bold"), 
    text_color="#FFFFFF"
)
Dado.grid(row=0, column=0, pady=(40, 0))

Boton_Numero = kc.CTkButton(
    Caja,
    text="TIRAR DADO",
    fg_color="#FFFFFF",
    text_color="#000000",
    font=("Comic Sans MS", 22, "bold"),
    hover_color="#E0E0E0",
    height=60,
    width=250,
    corner_radius=15,
    command=Tirada
)
Boton_Numero.grid(row=1, column=0, pady=(0, 40))

Root.mainloop()