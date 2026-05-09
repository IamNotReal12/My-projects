import customtkinter as kc
import qrcode as QR
from PIL import Image
from CTkColorPicker import *

kc.set_appearance_mode("dark")
kc.set_default_color_theme("blue")

App = kc.CTk()
App.title("QR Generator Pro")
App.after(0, lambda: App.state("zoomed"))

App.grid_columnconfigure((0, 1), weight=1)
App.grid_rowconfigure(0, weight=1)


def Color_fill():
    Color_selection = AskColor()
    color = Color_selection.get()

    if color:
        global qr_color_fill
        qr_color_fill = color
def Color_back():
    Color_Back = AskColor()
    Color_F_Back = Color_Back.get()
    
    
    if Color_F_Back:
        global Qr_color_Back
        Qr_color_Back = Color_F_Back
        
def Theme(valor):
    if valor == "Dark":
        kc.set_appearance_mode("dark")
        Subtitulo.configure(text_color="#FCF4F4")
        Caja_Frame.configure(fg_color="#333333")

    elif valor == "Light":

        kc.set_appearance_mode("light")
        Entry_convert.configure(text_color="#ffffff")
        Subtitulo.configure(text_color="#000000")
        Caja_Frame.configure(fg_color="#2c2a2a")


def CrearQR():
    contenido = str(Entry_convert.get().strip())
    global qr_color_fill,Qr_color_Back
    if not contenido:
        return

    qr = QR.QRCode(
        version=1, error_correction=QR.constants.ERROR_CORRECT_M, border=2, box_size=10
    )

    qr.add_data(contenido)
    qr.make(fit=True)

    img_pillow = qr.make_image(fill_color=qr_color_fill, back_color=Qr_color_Back).convert(
        "RGB"
    )

    Imagen_for_label = kc.CTkImage(
        light_image=img_pillow, dark_image=img_pillow, size=(250, 250)
    )

    label_Image.configure(image=Imagen_for_label)
    label_Image.image = Imagen_for_label

    Entry_convert.delete(0, "end")


FONT_TITULO = kc.CTkFont(family="Century Gothic", size=45, weight="bold")
FONT_ENTRY = kc.CTkFont(family="Century Gothic", size=16)
FONT_BOTON = kc.CTkFont(family="Century Gothic", size=18, weight="bold")


Contenedor = kc.CTkFrame(
    App, width=700, height=700, corner_radius=30, border_width=2, border_color="#6bde18"
)
Contenedor.grid(row=0, column=0, padx=20, pady=20)
Contenedor.grid_propagate(False)

Contenedor.grid_columnconfigure(0, weight=1)


Encabezado = kc.CTkLabel(
    Contenedor, text="QR GENERATOR", text_color="#6bde18", font=FONT_TITULO
)
Encabezado.grid(row=0, column=0, pady=(50, 10))

Subtitulo = kc.CTkLabel(
    Contenedor,
    text="Convierte tus links o textos instantáneamente",
    text_color="#FCF4F4",
    font=kc.CTkFont(family="Century Gothic", size=15),
)
Subtitulo.grid(row=1, column=0, pady=(0, 40))


Entry_convert = kc.CTkEntry(
    Contenedor,
    placeholder_text="Pega tu enlace o escribe aquí...",
    width=500,
    height=50,
    font=FONT_ENTRY,
    border_color="#6bde18",
    fg_color="#1A1A1A",
    corner_radius=15,
    justify="center",
)
Entry_convert.grid(row=2, column=0, pady=20)


Boton_Generar = kc.CTkButton(
    Contenedor,
    text="GENERAR CÓDIGO QR",
    width=300,
    height=60,
    corner_radius=15,
    fg_color="#6bde18",
    hover_color="#56b313",
    text_color="#000000",
    font=FONT_BOTON,
    command=CrearQR,
)
Boton_Generar.grid(row=3, column=0, pady=40)

Caja_Frame = kc.CTkFrame(Contenedor, width=250, height=250)
Caja_Frame.grid(row=4, column=0)
Caja_Frame.grid_propagate(False)

label_Image = kc.CTkLabel(Caja_Frame, text="")
label_Image.grid(row=0, column=0)

Tab_color = kc.CTkTabview(
    App, 
    width=400, 
    height=400, 
    fg_color="#1A1A1A", 
    segmented_button_selected_color="#6bde18",
    segmented_button_selected_hover_color="#56b313",
    segmented_button_unselected_color="#2b2b2b",
    text_color="#ffffff",
    corner_radius=25,
    border_width=2,
    border_color="#6bde18"
)
Tab_color.grid(row=0, column=1, padx=20, pady=20)

Tab_color.add("Modo")
Tab_color.add("Qrcolor")

Tab_color.tab("Modo").grid_columnconfigure(0, weight=1)

Colores = kc.CTkSegmentedButton(
    Tab_color.tab("Modo"),
    values=["Light", "Dark"],
    fg_color="#2b2b2b",
    selected_color="#6bde18",
    selected_hover_color="#56b313",
    text_color="#000000",
    unselected_color="#333333",
    unselected_hover_color="#444444",
    width=250,
    height=50,
    corner_radius=10,
    font=kc.CTkFont(family="Century Gothic", size=14, weight="bold"),
    command=Theme,
)
Colores.grid(row=0, column=0, padx=20, pady=60)
Colores.set("Dark")


Tab_color.tab("Qrcolor").grid_columnconfigure(0, weight=1)

button_color_fill = kc.CTkButton(
    Tab_color.tab("Qrcolor"), 
    text="🎨 COLOR DE RELLENO (FILL)", 
    command=Color_fill,
    width=250,
    height=50,
    corner_radius=12,
    fg_color="transparent",
    border_width=2,
    border_color="#6bde18",
    hover_color="#6bde18",
    text_color="#6bde18",
    font=kc.CTkFont(family="Century Gothic", size=13, weight="bold")
)
button_color_fill.grid(row=0, column=0, pady=(60, 10))

button_color_back = kc.CTkButton(
    Tab_color.tab("Qrcolor"), 
    text="🖼️ COLOR DE FONDO (BACK)", 
    command=Color_back,
    width=250,
    height=50,
    corner_radius=12,
    fg_color="transparent",
    border_width=2,
    border_color="#ffffff",
    hover_color="#ffffff",
    text_color="#ffffff",
    font=kc.CTkFont(family="Century Gothic", size=13, weight="bold")
)
button_color_back.grid(row=1, column=0, pady=10)
App.mainloop()
