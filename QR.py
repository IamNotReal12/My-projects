import customtkinter as kc
import qrcode as QR


kc.set_appearance_mode("dark")
kc.set_default_color_theme("blue")

App = kc.CTk()
App.title("QR Generator Pro")
App.after(0, lambda: App.state("zoomed"))

App.grid_columnconfigure(0, weight=1)
App.grid_rowconfigure(0, weight=1)

def CrearQR():
    contenido = str(Entry_convert.get())
    Entry_convert.delete(0,"end")
    qr = QR.QRCode(
        version=1,
        error_correction=QR.constants.ERROR_CORRECT_M,
        border=5,
        box_size=50
        
        
    )
    
    
    qr.add_data(contenido)
    qr.make(fit=True)
    
    imagen = qr.make_image(fill_color="#17d823",back_color="#ffffff")
    imagen.save("Ususarioqr.png")
    
FONT_TITULO = kc.CTkFont(family="Century Gothic", size=45, weight="bold")
FONT_ENTRY = kc.CTkFont(family="Century Gothic", size=16)
FONT_BOTON = kc.CTkFont(family="Century Gothic", size=18, weight="bold")


Contenedor = kc.CTkFrame(
    App, 
    width=700, 
    height=550, 
    corner_radius=30,
    border_width=2,
    border_color="#6bde18"
)
Contenedor.grid(row=0, column=0, padx=20, pady=20)
Contenedor.grid_propagate(False)

Contenedor.grid_columnconfigure(0, weight=1)




Encabezado = kc.CTkLabel(
    Contenedor, 
    text="QR GENERATOR", 
    text_color="#6bde18",
    font=FONT_TITULO
)
Encabezado.grid(row=0, column=0, pady=(50, 10))

Subtitulo = kc.CTkLabel(
    Contenedor, 
    text="Convierte tus links o textos instantáneamente", 
    text_color="#AAAAAA",
    font=kc.CTkFont(family="Century Gothic", size=15)
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
    justify="center"
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
    command=CrearQR
)
Boton_Generar.grid(row=3, column=0, pady=40)



App.mainloop()