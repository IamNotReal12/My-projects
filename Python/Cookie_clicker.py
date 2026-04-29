import customtkinter as kc
from PIL import Image

App = kc.CTk()
kc.set_appearance_mode("dark")
kc.set_default_color_theme("blue")


App.after(0, lambda: App.state("zoomed"))
App.grid_columnconfigure((0, 1), weight=1)
App.grid_rowconfigure(0, weight=1)


numero_contador = 0
valor_clic = 1


def Boton_Sumar():
    global numero_contador, valor_clic
    numero_contador += valor_clic
    Contador.configure(text=str(numero_contador))


def Boton_Resta():
    global numero_contador
    numero_contador -= 1
    if numero_contador < 0:
        numero_contador = 0
    Contador.configure(text=str(numero_contador))


def Boton_Resetear():
    global numero_contador
    numero_contador = 0
    Contador.configure(text=numero_contador)

def Label_Compra_Def():
    Label_Compra.configure(text="¡Mejora comprada!")
    Label_Compra.grid(row=2, column=0, pady=10)
    Label_Compra.after(2000, lambda: Label_Compra.grid_forget())

def Tienda_Def():
    global numero_contador, valor_clic

    if numero_contador >= 10:
        numero_contador -= 10
        valor_clic *= 2

        Contador.configure(text=str(numero_contador))
        Label_Compra_Def()



Frame_Contenido = kc.CTkFrame(
    App, width=500, height=400, corner_radius=20, border_width=2, border_color="#3B3B3B"
)
Frame_Contenido.grid(row=0, column=0)
Frame_Contenido.grid_propagate(False)
Frame_Contenido.grid_columnconfigure(0, weight=1)
Frame_Contenido.grid_rowconfigure((0, 1, 2, 3), weight=1)

FONT_LABEL = kc.CTkFont(family="Comic Sans MS", size=60, weight="bold")
FONT_LABEL_T = kc.CTkFont(family="Comic Sans MS", size=30, weight="bold")
FONT_BOTONES = kc.CTkFont(family="Arial", size=16, weight="bold")

Contador = kc.CTkLabel(Frame_Contenido, text="0", font=FONT_LABEL, text_color="#1F6AA5")
Contador.grid(row=1, column=0, pady=10)

Btn_Suma = kc.CTkButton(
    Frame_Contenido,
    text="SUMAR +1",
    font=FONT_BOTONES,
    fg_color="#2ECC71",
    hover_color="#27AE60",
    command=Boton_Sumar,
)
Btn_Suma.grid(row=2, column=0, pady=5)

Btn_Resta = kc.CTkButton(
    Frame_Contenido,
    text="RESTAR -1",
    font=FONT_BOTONES,
    fg_color="#E74C3C",
    hover_color="#C0392B",
    command=Boton_Resta,
)
Btn_Resta.grid(row=3, column=0, pady=5)

Btn_Reset = kc.CTkButton(
    Frame_Contenido,
    text="RESETEAR",
    font=FONT_BOTONES,
    fg_color="transparent",
    border_width=2,
    command=Boton_Resetear,
)
Btn_Reset.grid(row=4, column=0, pady=(5, 30))

Tienda = kc.CTkFrame(App, width=400, height=600, fg_color="transparent")
Tienda.grid(row=0, column=1)
Tienda.grid_propagate(False)
Tienda.grid_columnconfigure(0, weight=1)

Tienda_Header = kc.CTkLabel(Tienda, text="Tienda", font=FONT_LABEL)
Tienda_Header.grid(row=0, column=0)

Frame_Botones_Tienda = kc.CTkFrame(Tienda, width=300, height=200)
Frame_Botones_Tienda.grid(row=1, column=0, pady=20)

Btn_Suma = kc.CTkButton(
    Frame_Botones_Tienda,
    text="SUMAR X2",
    font=FONT_BOTONES,
    fg_color="#2ECC71",
    hover_color="#27AE60",
    command=Tienda_Def,
)
Btn_Suma.grid(row=0, column=0, pady=5)

Label_Compra = kc.CTkLabel(Tienda, text="", font=FONT_LABEL_T)

App.mainloop()
