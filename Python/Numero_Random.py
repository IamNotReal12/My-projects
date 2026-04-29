import customtkinter as kc
import random as rd

Root = kc.CTk()
kc.set_appearance_mode("dark")

Root.after(0, lambda: Root.state("zoomed"))
Root.grid_columnconfigure(0, weight=1)
Root.grid_rowconfigure(0, weight=1)

Numero_Secreto = rd.randint(1, 100)

def Tirada(event):
    
    try:
        Intento_Entry = int(Intento.get())
        if Intento_Entry == Numero_Secreto:
            Dado.configure(text=f"¡ADIVINASTE! Era el {Numero_Secreto}", text_color="#2ECC71")
            Dado.configure(font=("Comic Sans MS", 35, "bold"))
        elif Intento_Entry > Numero_Secreto:
            Dado.configure(text="Te has pasado 👇", text_color="#E74C3C")
            Dado.configure(font=("Comic Sans MS", 40, "bold"))
        elif Intento_Entry < Numero_Secreto:
            Dado.configure(text="Un poquito más 👆", text_color="#3498DB")    
            Dado.configure(font=("Comic Sans MS", 40, "bold"))
        
        Intento.delete(0, 'end') 
    except ValueError:
        Dado.configure(text="Pon un número", font=("Comic Sans MS", 40, "bold"))

Caja = kc.CTkFrame(
    Root, 
    width=600, 
    height=500, 
    corner_radius=30, 
    border_width=2, 
    border_color="#404040"
)
Caja.grid(row=0, column=0)
Caja.grid_propagate(False)
Caja.grid_columnconfigure(0, weight=1)
Caja.grid_rowconfigure((0, 1, 2), weight=1) # Añadí una fila más para equilibrio

Dado = kc.CTkLabel(
    Caja, 
    text="¿?", 
    font=("Comic Sans MS", 120, "bold"), 
    text_color="#FFFFFF"
)
Dado.grid(row=0, column=0, pady=(20, 0))

Intento = kc.CTkEntry(
    Caja,
    placeholder_text="Escribe un número (1-100) y pulsa ENTER",
    width=350,
    height=50,
    font=("Comic Sans MS", 16),
    justify="center",
    border_color="#1F6AA5",
    fg_color="#2B2B2B"
)
Intento.grid(row=1, column=0, pady=20)

Intento.bind("<Return>", Tirada)

# Instrucción extra abajo
Instruccion = kc.CTkLabel(Caja, text="Adivina el número secreto", font=("Arial", 12, "italic"), text_color="gray")
Instruccion.grid(row=2, column=0, pady=(0, 20))

Root.mainloop()