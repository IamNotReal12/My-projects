import customtkinter as kc
from PIL import Image

kc.set_appearance_mode("Dark")

App = kc.CTk()
App.after(0, lambda: App.state("zoomed"))
App.grid_columnconfigure(0, weight=1)
App.grid_rowconfigure(0, weight=1)

App.configure(fg_color="#0d0e12")

Amigos = Image.open("Amigos.png")

Imagen = kc.CTkImage(light_image=Amigos, dark_image=Amigos, size=(350, 350))


def actualizar_imagen(valor_automatico=None):

    ancho_actual = int(Slider_Ancho.get())
    alto_actual = int(Slider_Alto.get())

    Imagen.configure(size=(ancho_actual, alto_actual))

def descargar_imagen():
    ancho_final = int(Slider_Ancho.get())
    alto_final = int(Slider_Alto.get())
    
  
    imagen_espachurrada = Amigos.resize((ancho_final, alto_final))
    
    imagen_espachurrada.save("Amigos_Espachurrados.png")
    
   
    Boton_Descargar.configure(text="¡FOTO GUARDADA! 🎉", fg_color="#10b981")

Contenedor_principal = kc.CTkFrame(
    App,
    width=500,
    height=700,
    border_width=1,
    border_color="#1f293d",
    fg_color="#13141c",
    corner_radius=24,
)
Contenedor_principal.grid(row=0, column=0)
Contenedor_principal.grid_propagate(False)
Contenedor_principal.grid_columnconfigure(0, weight=1)
Contenedor_principal.grid_rowconfigure(1, weight=1)

Frame_Sliders = kc.CTkFrame(
    Contenedor_principal, width=400, height=200, fg_color="transparent"
)
Frame_Sliders.grid(row=0, column=0, sticky="n", pady=(40, 0))
Frame_Sliders.grid_propagate(False)
Frame_Sliders.grid_columnconfigure(0, weight=1)

Slider_Ancho = kc.CTkSlider(
    Frame_Sliders,
    button_color="#2563eb",
    button_hover_color="#1d4ed8",
    progress_color="#2563eb",
    fg_color="#1e293b",
    from_=10,
    to=350,
    command=actualizar_imagen
    
)
Slider_Ancho.grid(row=0, column=0, padx=(0, 15), pady=15, sticky="ew")
Slider_Ancho.set(350)
Label_Ancho = kc.CTkLabel(
    Frame_Sliders,
    text="Ancho",
    font=("Segoe UI", 13, "bold"),
    text_color="#94a3b8",
)
Label_Ancho.grid(row=0, column=1, sticky="w")

Slider_Alto = kc.CTkSlider(
    Frame_Sliders,
    button_color="#2563eb",
    button_hover_color="#1d4ed8",
    progress_color="#2563eb",
    fg_color="#1e293b",
    command=actualizar_imagen,
    from_=10,
    to=350,
)
Slider_Alto.grid(row=1, column=0, padx=(0, 15), pady=15, sticky="ew")
Slider_Alto.set(350)
Label_Alto = kc.CTkLabel(
    Frame_Sliders,
    text="Alto",
    font=("Segoe UI", 13, "bold"),
    text_color="#94a3b8",
)
Label_Alto.grid(row=1, column=1, sticky="w")

Frame_Imagen = kc.CTkFrame(
    Contenedor_principal,
    width=400,
    height=400,
    fg_color="#090a0f",
    corner_radius=16,
    border_width=2,
    border_color="#1f293d",
)
Frame_Imagen.grid(row=1, column=0, pady=(0, 40))
Frame_Imagen.grid_columnconfigure(0, weight=1)
Frame_Imagen.grid_rowconfigure(0, weight=1)
Frame_Imagen.grid_propagate(False)

Label_Image = kc.CTkLabel(Frame_Imagen, text="", image=Imagen, compound="center")
Label_Image.grid(row=0, column=0)
Boton_Descargar = kc.CTkButton(
    Contenedor_principal,
    text="📥 Descargar Monstruosidad",
    font=("Segoe UI", 14, "bold"),
    width=350,
    height=40,
    corner_radius=12,
    fg_color="#2563eb",
    hover_color="#1d4ed8",
    command=descargar_imagen 
)
Boton_Descargar.grid(row=1, column=0, pady=(10, 20),sticky="s")
App.mainloop()
